// Tour de Suisse Legends Dataset (84 riders × 6 eras)
// Tour de Suisse = 1933-present (93 years history)
// "Race of the Helvetia" - premier Swiss stage race, often Tour de France warm-up

const ERA_NAMES = {
    1: "1930s-60s",
    2: "1970s-80s",
    3: "1990s",
    4: "2000s",
    5: "2010s",
    6: "2020s"
};

const ERA_LABELS = {
    1: "33-69",
    2: "70-89",
    3: "90-99",
    4: "00-09",
    5: "10-19",
    6: "20-now"
};

// Format: { name, era, pos, ovr }
// pos = GC / TT / SPR / CLIM / PUR (Pure climber) / HILL
// Tour de Suisse stars tend to be strong TT/GC riders (Swiss cycling = time trial culture)

const DRIVERS = [
    // Era 1: 1930s-60s (pre-modern)
    { name: "Hans Knecht", era: 1, pos: "GC", ovr: 70 },
    { name: "Ferdi Kübler", era: 1, pos: "CLIM", ovr: 78 },
    { name: "Hugo Koblet", era: 1, pos: "TT", ovr: 85 },
    { name: "Carlo Clerici", era: 1, pos: "HILL", ovr: 72 },
    { name: "Pasquale Fornara", era: 1, pos: "GC", ovr: 71 },
    { name: "Attilio Reda", era: 1, pos: "HILL", ovr: 70 },
    { name: "Rolf Graf", era: 1, pos: "TT", ovr: 73 },
    { name: "Max Bulla", era: 1, pos: "SPR", ovr: 71 },
    { name: "Josef Beyaert", era: 1, pos: "GC", ovr: 70 },
    { name: "Roger Rivière", era: 1, pos: "TT", ovr: 80 },
    { name: "Jacques Anquetil", era: 1, pos: "TT", ovr: 92 },
    { name: "Rudi Altig", era: 1, pos: "SPR", ovr: 82 },
    { name: "Vittorio Adorni", era: 1, pos: "TT", ovr: 78 },
    { name: "Felice Gimondi", era: 1, pos: "GC", ovr: 84 },

    // Era 2: 1970s-80s
    { name: "Eddy Merckx", era: 2, pos: "GC", ovr: 99 },
    { name: "Bernard Hinault", era: 2, pos: "GC", ovr: 96 },
    { name: "Joop Zoetemelk", era: 2, pos: "GC", ovr: 85 },
    { name: "Francesco Moser", era: 2, pos: "TT", ovr: 86 },
    { name: "Gianni Bugno", era: 2, pos: "GC", ovr: 84 },
    { name: "Urs Zimmermann", era: 2, pos: "TT", ovr: 82 },
    { name: "Tony Rominger", era: 2, pos: "TT", ovr: 88 },
    { name: "Pedro Delgado", era: 2, pos: "CLIM", ovr: 87 },
    { name: "Laurent Fignon", era: 2, pos: "TT", ovr: 87 },
    { name: "Robert Millar", era: 2, pos: "CLIM", ovr: 84 },
    { name: "Stephen Roche", era: 2, pos: "GC", ovr: 85 },
    { name: "Andy Hampsten", era: 2, pos: "CLIM", ovr: 82 },
    { name: "Phil Anderson", era: 2, pos: "HILL", ovr: 80 },
    { name: "Steven Rooks", era: 2, pos: "CLIM", ovr: 81 },

    // Era 3: 1990s
    { name: "Miguel Indurain", era: 3, pos: "TT", ovr: 95 },
    { name: "Alex Zülle", era: 3, pos: "TT", ovr: 88 },
    { name: "Pascal Richard", era: 3, pos: "GC", ovr: 81 },
    { name: "Beat Zberg", era: 3, pos: "HILL", ovr: 75 },
    { name: "Marco Pantani", era: 3, pos: "PUR", ovr: 91 },
    { name: "Jan Ullrich", era: 3, pos: "TT", ovr: 92 },
    { name: "Bjarne Riis", era: 3, pos: "CLIM", ovr: 83 },
    { name: "Richard Virenque", era: 3, pos: "CLIM", ovr: 84 },
    { name: "Laurent Jalabert", era: 3, pos: "HILL", ovr: 88 },
    { name: "Frank Vandenbroucke", era: 3, pos: "HILL", ovr: 82 },
    { name: "Laurent Dufaux", era: 3, pos: "GC", ovr: 80 },
    { name: "Luc Leblanc", era: 3, pos: "HILL", ovr: 78 },
    { name: "Steffen Wesemann", era: 3, pos: "HILL", ovr: 76 },
    { name: "Niki Rüttimann", era: 3, pos: "GC", ovr: 74 },

    // Era 4: 2000s
    { name: "Lance Armstrong", era: 4, pos: "TT", ovr: 95 },
    { name: "Floyd Landis", era: 4, pos: "TT", ovr: 82 },
    { name: "Andreas Klöden", era: 4, pos: "TT", ovr: 85 },
    { name: "Levi Leipheimer", era: 4, pos: "TT", ovr: 84 },
    { name: "Michael Rogers", era: 4, pos: "TT", ovr: 80 },
    { name: "Fränk Schleck", era: 4, pos: "GC", ovr: 82 },
    { name: "Andy Schleck", era: 4, pos: "CLIM", ovr: 86 },
    { name: "Roman Kreuziger", era: 4, pos: "GC", ovr: 80 },
    { name: "Vincenzo Nibali", era: 4, pos: "GC", ovr: 88 },
    { name: "Samuel Sánchez", era: 4, pos: "CLIM", ovr: 83 },
    { name: "Damiano Cunego", era: 4, pos: "CLIM", ovr: 84 },
    { name: "Alessandro Ballan", era: 4, pos: "HILL", ovr: 81 },
    { name: "Óscar Freire", era: 4, pos: "SPR", ovr: 86 },
    { name: "Mark Cavendish", era: 4, pos: "SPR", ovr: 90 },

    // Era 5: 2010s
    { name: "Chris Froome", era: 5, pos: "CLIM", ovr: 94 },
    { name: "Alberto Contador", era: 5, pos: "GC", ovr: 92 },
    { name: "Fabian Cancellara", era: 5, pos: "TT", ovr: 90 },
    { name: "Rui Costa", era: 5, pos: "GC", ovr: 82 },
    { name: "Geraint Thomas", era: 5, pos: "GC", ovr: 86 },
    { name: "Simon Spilak", era: 5, pos: "GC", ovr: 80 },
    { name: "Damiano Caruso", era: 5, pos: "CLIM", ovr: 81 },
    { name: "Peter Sagan", era: 5, pos: "HILL", ovr: 93 },
    { name: "Tom Dumoulin", era: 5, pos: "TT", ovr: 89 },
    { name: "Primož Roglič", era: 5, pos: "GC", ovr: 91 },
    { name: "Michael Matthews", era: 5, pos: "HILL", ovr: 85 },
    { name: "Julian Alaphilippe", era: 5, pos: "HILL", ovr: 90 },
    { name: "Nairo Quintana", era: 5, pos: "CLIM", ovr: 86 },
    { name: "Thibaut Pinot", era: 5, pos: "CLIM", ovr: 85 },

    // Era 6: 2020s
    { name: "Tadej Pogačar", era: 6, pos: "GC", ovr: 99 },
    { name: "Jonas Vingegaard", era: 6, pos: "GC", ovr: 96 },
    { name: "Remco Evenepoel", era: 6, pos: "TT", ovr: 95 },
    { name: "Juan Ayuso", era: 6, pos: "GC", ovr: 86 },
    { name: "Adam Yates", era: 6, pos: "GC", ovr: 84 },
    { name: "Enric Mas", era: 6, pos: "CLIM", ovr: 85 },
    { name: "Mattias Skjelmose", era: 6, pos: "GC", ovr: 84 },
    { name: "Marc Hirschi", era: 6, pos: "HILL", ovr: 84 },
    { name: "Richard Carapaz", era: 6, pos: "CLIM", ovr: 87 },
    { name: "Wout van Aert", era: 6, pos: "HILL", ovr: 92 },
    { name: "Mathieu van der Poel", era: 6, pos: "HILL", ovr: 93 },
    { name: "Egan Bernal", era: 6, pos: "GC", ovr: 87 },
    { name: "Mikel Landa", era: 6, pos: "CLIM", ovr: 84 },
    { name: "Sepp Kuss", era: 6, pos: "CLIM", ovr: 84 }
];

// 2026 Tour de Suisse schedule (8 stages)
// Tour de Suisse is known for: ITT/mountain/hill mix, climbing stages in Swiss Alps
// Format: Prologue → 1 sprint → 2-3 mountain → 1-2 hills → 1 ITT → 1 mountain finish
const SCHEDULE = [
    { stage: 1, name: "Küsnacht Prologue", type: "ITT", desc: "Short opening TT, technical" },
    { stage: 2, name: "Basel Sprint", type: "flat", desc: "Fast opener, mass sprint expected" },
    { stage: 3, name: "Emmental Hills", type: "hills", desc: "Rolling terrain, punchy climbs" },
    { stage: 4, name: "Nufenen Pass", type: "mountain", desc: "High alpine, GC battle begins" },
    { stage: 5, name: "Andermatt Summit", type: "mountain", desc: "Mountain stage, summit finish" },
    { stage: 6, name: "Gstaad Hills", type: "hills", desc: "Mid-mountain, breakaway territory" },
    { stage: 7, name: "Andeer ITT", type: "ITT", desc: "30km time trial, GC shake-up" },
    { stage: 8, name: "Andermatt Mountain", type: "mountain", desc: "Final mountain, GC showdown" }
];
