// Test.js — Tour de Suisse 8-0 Monte Carlo validation
const fs = require('fs');
const html = fs.readFileSync('/tmp/build_suisse/output.html', 'utf8');
const m = html.match(/<script>([\s\S]*?)<\/script>/);
if (!m) { console.log('ERROR: no <script> tag found'); process.exit(1); }
const code = m[1];

// Mock DOM
const noop = () => {};
const fakeCtx = new Proxy({}, { get: () => noop });
const fakeEl = {
  classList: { add: noop, remove: noop, contains: () => false },
  innerHTML: '', textContent: '',
  appendChild: noop, querySelectorAll: () => [],
  scrollTop: 0, scrollHeight: 0, style: {},
  dataset: {},
};
global.document = {
  getElementById: () => fakeEl,
  querySelectorAll: () => [],
  createElement: () => ({ className: '', innerHTML: '', onclick: null, appendChild: noop, style: {} }),
};
global.setTimeout = noop;
global.localStorage = { getItem: () => null, setItem: noop };

// Wrap code + expose API
const fn = new Function('document', 'setTimeout', 'localStorage',
  code + '; return { DRIVERS, SCHEDULE, simulateRace, pointsForPos, ERA_NAMES, ERA_LABELS, mulberry32 };');
const api = fn(global.document, global.setTimeout, global.localStorage);

console.log('=== Tour de Suisse 8-0 Monte Carlo Test ===');
console.log('DRIVERS count:', api.DRIVERS ? api.DRIVERS.length : 'UNDEFINED');
console.log('SCHEDULE count:', api.SCHEDULE ? api.SCHEDULE.length : 'UNDEFINED');
console.log('ERA_NAMES:', JSON.stringify(api.ERA_NAMES));

// Test single race
console.log('\n=== Single race test (5 OVRs × 5 stage types × 50 sims) ===');
for (const ovr of [70, 80, 90, 95, 99]) {
  for (const stage of api.SCHEDULE) {
    let wins = 0;
    for (let seed = 1; seed <= 50; seed++) {
      const rng = api.mulberry32(seed);
      const r = api.simulateRace(ovr, stage.type, rng);
      if (r.playerPos === 1) wins++;
    }
    const total = 50;
    const pct = (wins / total * 100).toFixed(0);
    console.log(`  OVR ${ovr} ${stage.type.padEnd(8)} (${stage.name.padEnd(22)}): ${wins}/${total} (${pct}%)`);
  }
  console.log('');
}

// Test full season
console.log('\n=== Full season test (8 stages × 100 sims) ===');
for (const ovr of [70, 80, 85, 90, 95, 99]) {
  let perfect = 0;
  let totalWins = 0;
  for (let seed = 1; seed <= 200; seed++) {
    const rng = api.mulberry32(seed);
    let wins = 0;
    for (let i = 0; i < api.SCHEDULE.length; i++) {
      const stage = api.SCHEDULE[i];
      const r = api.simulateRace(ovr, stage.type, rng);
      if (r.playerPos === 1) wins++;
    }
    totalWins += wins;
    if (wins === api.SCHEDULE.length) perfect++;
  }
  const avg = (totalWins / 200).toFixed(2);
  const perfectPct = (perfect / 200 * 100).toFixed(2);
  console.log(`  OVR ${ovr}: avg wins = ${avg}/${api.SCHEDULE.length}, perfect 8-0 = ${perfect}/200 (${perfectPct}%)`);
}
