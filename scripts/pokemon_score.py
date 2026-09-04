#!/usr/bin/env python3
"""Score every Pokémon answer on "Pokémon-ness" and write the ledger.

The premise: an answer that reaches for *named* Pokémon entities — real species,
real moves, real items, real abilities, real characters and real places — is doing
more analogy work than one that leans on generic furniture ("a Trainer", "a Gym",
"a battle"). Generic terms still count, but only as the denominator.

Score (0-100) = breadth + density + specificity

  breadth      0-45   how many DISTINCT named entities the answer uses
  density      0-35   named-entity mentions per 100 words
  specificity  0-20   named / (named + generic) mentions

Usage:
    python3 scripts/pokemon_score.py              # print table, write LEDGER.md
    python3 scripts/pokemon_score.py --json       # machine-readable
    python3 scripts/pokemon_score.py --detail 042 # show what one answer matched
"""

from __future__ import annotations

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------- vocabularies

SPECIES = """
Bulbasaur Ivysaur Venusaur Charmander Charmeleon Charizard Squirtle Wartortle
Blastoise Caterpie Metapod Butterfree Weedle Beedrill Pidgey Pidgeot Rattata
Raticate Spearow Fearow Ekans Arbok Pikachu Raichu Sandshrew Nidoking Nidoqueen
Clefairy Vulpix Ninetales Jigglypuff Zubat Golbat Crobat Oddish Gloom Vileplume
Paras Venonat Diglett Dugtrio Meowth Persian Psyduck Golduck Mankey Primeape
Growlithe Arcanine Poliwag Poliwhirl Poliwrath Politoed Abra Kadabra Alakazam
Machop Machoke Machamp Bellsprout Tentacool Tentacruel Geodude Graveler Golem
Ponyta Rapidash Slowpoke Slowbro Magnemite Magneton Farfetch Doduo Dodrio Seel
Dewgong Grimer Muk Shellder Cloyster Gastly Haunter Gengar Onix Drowzee Hypno
Krabby Kingler Voltorb Electrode Exeggcute Exeggutor Cubone Marowak Hitmonlee
Hitmonchan Lickitung Koffing Weezing Rhyhorn Rhydon Rhyperior Chansey Blissey
Happiny Tangela Kangaskhan Horsea Seadra Kingdra Goldeen Seaking Staryu Starmie
Scyther Scizor Jynx Electabuzz Magmar Pinsir Tauros Magikarp Gyarados Lapras
Ditto Eevee Vaporeon Jolteon Flareon Espeon Umbreon Leafeon Glaceon Sylveon
Porygon Omanyte Kabuto Aerodactyl Snorlax Articuno Zapdos Moltres Dratini
Dragonair Dragonite Mewtwo Mew Chikorita Cyndaquil Typhlosion Totodile
Feraligatr Sentret Hoothoot Ledyba Spinarak Ariados Chinchou Lanturn Pichu
Cleffa Igglybuff Togepi Togekiss Natu Xatu Mareep Flaaffy Ampharos Bellossom
Marill Azumarill Sudowoodo Hoppip Aipom Sunkern Yanma Wooper Quagsire Murkrow
Misdreavus Unown Wobbuffet Wynaut Girafarig Pineco Forretress Dunsparce Gligar
Steelix Snubbull Granbull Qwilfish Shuckle Heracross Sneasel Weavile Teddiursa
Ursaring Slugma Magcargo Swinub Piloswine Mamoswine Corsola Remoraid Octillery
Delibird Mantine Skarmory Houndour Houndoom Phanpy Donphan Stantler Smeargle
Tyrogue Hitmontop Smoochum Elekid Magby Miltank Raikou Entei Suicune Larvitar
Pupitar Tyranitar Lugia Celebi Treecko Sceptile Torchic Blaziken Mudkip
Swampert Poochyena Mightyena Zigzagoon Linoone Wurmple Beautifly Dustox Lotad
Ludicolo Seedot Shiftry Taillow Swellow Wingull Pelipper Ralts Kirlia Gardevoir
Gallade Surskit Masquerain Shroomish Breloom Slakoth Vigoroth Slaking Nincada
Ninjask Shedinja Whismur Loudred Exploud Makuhita Hariyama Azurill Nosepass
Skitty Delcatty Sableye Mawile Aron Lairon Aggron Meditite Medicham Electrike
Manectric Plusle Minun Volbeat Illumise Roselia Roserade Gulpin Swalot Carvanha
Sharpedo Wailmer Wailord Numel Camerupt Torkoal Spoink Grumpig Spinda Trapinch
Vibrava Flygon Cacnea Cacturne Swablu Altaria Zangoose Seviper Lunatone Solrock
Barboach Whiscash Corphish Crawdaunt Baltoy Claydol Lileep Cradily Anorith
Armaldo Feebas Milotic Castform Kecleon Shuppet Banette Duskull Dusclops
Dusknoir Tropius Chimecho Absol Snorunt Glalie Froslass Spheal Sealeo Walrein
Clamperl Huntail Gorebyss Relicanth Luvdisc Bagon Shelgon Salamence Beldum
Metang Metagross Regirock Regice Registeel Latias Latios Kyogre Groudon
Rayquaza Jirachi Deoxys Turtwig Grotle Torterra Chimchar Monferno Infernape
Piplup Prinplup Empoleon Staraptor Bidoof Bibarel Kricketot Shinx Luxray
Budew Cranidos Rampardos Shieldon Bastiodon Burmy Wormadam Mothim Combee
Vespiquen Pachirisu Buizel Floatzel Cherubi Cherrim Shellos Gastrodon Ambipom
Drifloon Drifblim Buneary Lopunny Mismagius Honchkrow Glameow Purugly Chingling
Stunky Skuntank Bronzor Bronzong Bonsly Mime Happiny Chatot Spiritomb Gible
Gabite Garchomp Riolu Lucario Hippopotas Hippowdon Skorupi Drapion Croagunk
Toxicroak Carnivine Finneon Lumineon Snover Abomasnow Magnezone Lickilicky
Tangrowth Electivire Magmortar Yanmega Gliscor Porygon-Z Dusknoir Froslass
Rotom Uxie Mesprit Azelf Dialga Palkia Heatran Regigigas Giratina Cresselia
Phione Manaphy Darkrai Shaymin Arceus Victini Snivy Serperior Tepig Emboar
Oshawott Samurott Patrat Watchog Lillipup Herdier Stoutland Purrloin Liepard
Pansage Pansear Panpour Munna Musharna Pidove Tranquill Unfezant Blitzle
Zebstrika Roggenrola Boldore Gigalith Woobat Swoobat Drilbur Excadrill Audino
Timburr Gurdurr Conkeldurr Tympole Palpitoad Seismitoad Throh Sawk Sewaddle
Swadloon Leavanny Venipede Whirlipede Scolipede Cottonee Whimsicott Petilil
Lilligant Basculin Sandile Krokorok Krookodile Darumaka Darmanitan Maractus
Dwebble Crustle Scraggy Scrafty Sigilyph Yamask Cofagrigus Tirtouga Carracosta
Archen Archeops Trubbish Garbodor Zorua Zoroark Minccino Cinccino Gothita
Solosis Reuniclus Ducklett Swanna Vanillite Vanilluxe Deerling Sawsbuck Emolga
Karrablast Escavalier Foongus Amoonguss Frillish Jellicent Alomomola Joltik
Galvantula Ferroseed Ferrothorn Klink Klang Klinklang Tynamo Eelektross Elgyem
Beheeyem Litwick Lampent Chandelure Axew Fraxure Haxorus Cubchoo Beartic
Cryogonal Shelmet Accelgor Stunfisk Mienfoo Mienshao Druddigon Golett Golurk
Pawniard Bisharp Bouffalant Rufflet Braviary Vullaby Mandibuzz Heatmor Durant
Deino Zweilous Hydreigon Larvesta Volcarona Cobalion Terrakion Virizion
Tornadus Thundurus Reshiram Zekrom Landorus Kyurem Keldeo Meloetta Genesect
Chespin Fennekin Froakie Greninja Bunnelby Fletchling Talonflame Pancham
Pangoro Furfrou Espurr Meowstic Honedge Doublade Aegislash Spritzee Aromatisse
Swirlix Slurpuff Inkay Malamar Binacle Barbaracle Skrelp Dragalge Clauncher
Clawitzer Helioptile Heliolisk Tyrunt Tyrantrum Amaura Aurorus Sylveon Hawlucha
Dedenne Carbink Goomy Sliggoo Goodra Klefki Phantump Trevenant Pumpkaboo
Gourgeist Bergmite Avalugg Noibat Noivern Xerneas Yveltal Zygarde Diancie
Hoopa Volcanion Rowlet Decidueye Litten Incineroar Popplio Primarina Yungoos
Grubbin Charjabug Vikavolt Crabrawler Oricorio Cutiefly Ribombee Rockruff
Lycanroc Wishiwashi Mareanie Toxapex Mudbray Mudsdale Dewpider Araquanid
Fomantis Lurantis Morelull Shiinotic Salandit Salazzle Stufful Bewear Bounsweet
Comfey Oranguru Passimian Wimpod Golisopod Sandygast Palossand Pyukumuku
Minior Komala Turtonator Togedemaru Mimikyu Bruxish Drampa Dhelmise Jangmo
Hakamo Kommo Tapu Cosmog Solgaleo Lunala Nihilego Buzzwole Pheromosa Xurkitree
Celesteela Kartana Guzzlord Necrozma Magearna Marshadow Zeraora Grookey
Rillaboom Scorbunny Cinderace Sobble Inteleon Corviknight Orbeetle Nickit
Gossifleur Wooloo Dubwool Yamper Boltund Rolycoly Carkol Coalossal Applin
Flapple Appletun Silicobra Sandaconda Cramorant Toxel Toxtricity Sizzlipede
Centiskorch Clobbopus Grapploct Sinistea Polteageist Hatenna Hatterene Impidimp
Grimmsnarl Obstagoon Perrserker Cursola Sirfetch Runerigus Milcery Alcremie
Falinks Pincurchin Snom Frosmoth Stonjourner Eiscue Indeedee Morpeko Cufant
Copperajah Dracozolt Arctozolt Dracovish Arctovish Duraludon Dreepy Drakloak
Dragapult Zacian Zamazenta Eternatus Kubfu Urshifu Zarude Regieleki Regidrago
Glastrier Spectrier Calyrex Sprigatito Meowscarada Fuecoco Skeledirge Quaxly
Quaquaval Lechonk Oinkologne Tarountula Nymble Lokix Pawmi Pawmot Tandemaus
Maushold Fidough Dachsbun Smoliv Arboliva Squawkabilly Nacli Naclstack
Garganacl Charcadet Armarouge Ceruledge Tadbulb Bellibolt Wattrel Kilowattrel
Maschiff Mabosstiff Shroodle Grafaiai Bramblin Brambleghast Toedscool
Klawf Capsakid Scovillain Rellor Rabsca Flittle Espathra Tinkatink Tinkaton
Wiglett Bombirdier Finizen Palafin Varoom Revavroom Cyclizar Orthworm Glimmet
Glimmora Greavard Houndstone Flamigo Cetoddle Cetitan Veluza Dondozo
Tatsugiri Annihilape Clodsire Farigiraf Dudunsparce Kingambit Great Tusk
Iron Treads Baxcalibur Gimmighoul Gholdengo Wo-Chien Chien-Pao Ting-Lu Chi-Yu
Roaring Moon Iron Valiant Koraidon Miraidon Walking Wake Iron Leaves
""".split()

MOVES = """
Thunderbolt, Thunder, Thunder Wave, Volt Switch, Quick Attack, Iron Tail, Splash,
Flamethrower, Fire Blast, Smokescreen, Dragon Rage, Dragon Dance, Dragon Claw,
Dragon Tail, Outrage, Dragon Pulse, Draco Meteor, Ember, Crunch, Waterfall,
Aqua Tail, Hydro Pump, Water Gun, Rain Dance, Sunny Day, Sandstorm, Swords Dance,
Nasty Plot, Calm Mind, Bulk Up, Stealth Rock, Toxic Spikes, Sticky Web,
Rapid Spin, Defog, Substitute, Softboiled, Trick Room, Tailwind, Light Screen,
Aurora Veil, Rock Slide, Rock Tomb, Stone Edge, Earthquake, Earth Power,
Power Whip, Leech Seed, Giga Drain, Energy Ball, Solar Beam, Sludge Bomb,
Will-O-Wisp, Thunder Punch, Fire Punch, Ice Punch, Close Combat, Brick Break,
Drain Punch, Mach Punch, Extreme Speed, Aqua Jet, Shadow Ball, Dark Pulse,
Knock Off, Sucker Punch, Foul Play, Psyshock, Moonblast, Dazzling Gleam,
Play Rough, Flash Cannon, Iron Head, Gyro Ball, Body Slam, Double-Edge,
Explosion, Self-Destruct, Hyper Beam, Giga Impact, U-turn, Baton Pass,
Double Team, Tail Whip, Sweet Kiss, Nuzzle, Endeavor, Flail, Destiny Bond,
Perish Song, Whirlwind, Fake Out, Follow Me, Rage Powder, Helping Hand,
Icy Wind, Ice Beam, Blizzard, Freeze-Dry, Scald, Muddy Water, Heat Wave,
Eruption, Water Spout, Overheat, Leaf Storm, Hurricane, Air Slash, Brave Bird,
Acrobatics, Bullet Punch, Sacred Sword, Sleep Powder, Stun Spore, Confuse Ray,
Toxic, Synthesis, Moonlight, Protect, Detect, Recover, Roost, Surf, Slash,
Scratch, Growl, Leer, Tackle, Bite, Agility, Spikes, Encore, Taunt, Disable,
Yawn, Spore, Psychic, Facade, Wish, Charm, Feint, Rage, Harden, Withdraw,
Thrash, Struggle, Splash, Metronome, Transform, Teleport, Dig, Fly, Cut,
Strength, Flash, Rock Smash, Whirlpool, Waterfall, Headbutt, Curse, Amnesia,
Belly Drum, Counter, Mirror Coat, Pain Split, Trick, Switcheroo, Volt Tackle
"""

ITEMS = """
Poké Ball, Great Ball, Ultra Ball, Master Ball, Quick Ball, Dusk Ball,
Timer Ball, Net Ball, Heal Ball, Luxury Ball, Beast Ball, Super Potion,
Hyper Potion, Max Potion, Full Restore, Max Revive, Full Heal, Rare Candy,
Leftovers, Focus Sash, Focus Band, Choice Band, Choice Scarf, Choice Specs,
Life Orb, Assault Vest, Eviolite, Rocky Helmet, Air Balloon, Weakness Policy,
Mystic Water, Charcoal, Miracle Seed, Twisted Spoon, Black Belt, Sharp Beak,
Poison Barb, Soft Sand, Hard Stone, Silver Powder, Spell Tag, Dragon Fang,
Metal Coat, Black Glasses, Never-Melt Ice, Silk Scarf, Damp Rock, Heat Rock,
Smooth Rock, Icy Rock, Light Clay, Terrain Extender, Booster Energy,
Sitrus Berry, Lum Berry, Chesto Berry, Oran Berry, Leppa Berry, Exp. Share,
Amulet Coin, Everstone, Light Ball, Thick Club, Metronome, Shell Bell,
Berry Juice, Antidote
"""

ABILITIES = """
Sturdy, Levitate, Intimidate, Drizzle, Drought, Sand Stream, Snow Warning,
Swift Swim, Chlorophyll, Sand Rush, Slush Rush, Flash Fire, Water Absorb,
Volt Absorb, Huge Power, Adaptability, Technician, Skill Link, Serene Grace,
Speed Boost, Moxie, Multiscale, Regenerator, Magic Guard, Wonder Guard,
Flame Body, Poison Point, Rough Skin, Iron Barbs, Prankster, Defiant,
Competitive, Justified, Solar Power, Dry Skin, Thick Fat, Solid Rock,
Clear Body, Soundproof, Overgrow, Blaze, Torrent, Swarm, Shed Skin,
Natural Cure, Own Tempo, Inner Focus, Cursed Body, Protean, Libero,
Beast Boost, Grassy Surge, Misty Surge, Electric Surge, Psychic Surge,
Good as Gold, Quark Drive, Protosynthesis, Supreme Overlord, Unnerve
"""

CHARACTERS = """
Brock, Misty, Lt. Surge, Erika, Koga, Sabrina, Blaine, Giovanni, Falkner,
Bugsy, Whitney, Morty, Chuck, Jasmine, Pryce, Clair, Roxanne, Brawly, Wattson,
Flannery, Norman, Winona, Tate, Liza, Wallace, Juan, Roark, Gardenia, Maylene,
Crasher Wake, Fantina, Byron, Candice, Volkner, Cheren, Roxie, Burgh, Elesa,
Clay, Skyla, Brycen, Drayden, Viola, Korrina, Ramos, Clemont, Valerie, Olympia,
Wulfric, Ilima, Lana, Kiawe, Mallow, Sophocles, Acerola, Milo, Nessa, Kabu,
Allister, Opal, Gordie, Melony, Piers, Raihan, Katy, Brassius, Iono, Kofu,
Ryme, Tulip, Grusha, Lorelei, Bruno, Agatha, Lance, Sidney, Phoebe, Glacia,
Drake, Aaron, Bertha, Flint, Lucian, Shauntal, Grimsley, Caitlin, Malva,
Siebold, Wikstrom, Drasna, Hala, Olivia, Nanu, Hapu, Rika, Poppy, Hassel,
Steven, Cynthia, Alder, Diantha, Leon, Geeta, Nemona, Professor Oak, Team Rocket,
Nurse Joy, Officer Jenny
"""

PLACES = """
Pewter City, Cerulean City, Vermilion City, Celadon City, Fuchsia City,
Saffron City, Cinnabar Island, Viridian City, Pallet Town, Lavender Town,
Indigo Plateau, Victory Road, Mt. Moon, Rock Tunnel, Safari Zone, Silph Co.,
Cerulean Cave, Ecruteak City, Goldenrod City, Blackthorn City, Olivine City,
Azalea Town, Sootopolis City, Mauville City, Rustboro City, Lilycove City,
Battle Frontier, Battle Tower, Battle Maison, Pokémon Center, Pokémon League,
Elite Four, Day Care, Hoenn, Sinnoh, Unova, Kalos, Alola, Galar, Paldea,
Route 1, Tall Grass, PC box
"""

MECHANICS = """
Flat Rules, VGC, Regulation G, Effort Values, EVs, IVs, Individual Values,
Base Stat Total, Type Chart, Super Effective, STAB, Critical Hit, Shiny,
Hidden Ability, Mega Evolution, Terastallize, Dynamax, Z-Move, Speed Tier,
Entry Hazard, Held Item, Poké Ball, Stat Stage, Four-Move Limit
"""


def _clean(raw):
    """Split a comma-separated vocabulary block into a set of terms."""
    if isinstance(raw, str):
        parts = raw.replace("\n", " ").split(",")
    else:
        parts = raw
    return {p.strip() for p in parts if p.strip()}


NAMED: dict[str, set[str]] = {
    "species": _clean(SPECIES),
    "move": _clean(MOVES),
    "item": _clean(ITEMS),
    "ability": _clean(ABILITIES),
    "character": _clean(CHARACTERS),
    "place": _clean(PLACES),
    "mechanic": _clean(MECHANICS),
}

# Generic Pokémon furniture: counts, but only as the denominator.
GENERIC = {
    "pokémon", "pokemon", "trainer", "trainers", "gym", "gyms", "gym leader",
    "gym leaders", "badge", "badges", "battle", "battles", "battling", "type",
    "types", "level", "levels", "party", "pc box", "champion", "champions",
    "league", "move", "moves", "moveset", "faint", "fainted", "fainting",
    "switch", "switching", "turn", "turns", "coach", "coaches", "roster",
    "matchup", "matchups", "opponent", "opponents", "hp", "attack", "defence",
    "defense", "speed", "stat", "stats", "team", "teams", "wild", "grass",
    "evolve", "evolves", "evolution", "catch", "caught", "scout", "scouting",
    "tournament", "tournaments", "match", "matches", "referee", "referees",
}

# Words that are too ambiguous to count as named entities on their own.
AMBIGUOUS = {
    # Matching is case-sensitive, so a capitalised move name ("Protect", "Surf")
    # is already unambiguous here. These are the terms that stay risky even
    # capitalised — ordinary words, or names that collide with common English.
    "Blue", "Red", "Will", "Karen", "James", "Grant", "Larry", "Iris", "Bea",
    "Marshal", "Clay", "Milo", "Lana", "Viola", "Steven", "Leon", "Nature",
    "Weather", "Terrain", "Static", "Pressure", "Simple", "Contrary", "Unaware",
    "Immunity", "Trace", "Download", "Filter", "Analytic", "Speed", "Toxic",
    "Blaze", "Torrent", "Swarm", "Defiant", "Competitive", "Justified",
    "Held Item", "Super Effective",
}
for group in NAMED.values():
    group -= AMBIGUOUS

def body_of(path: pathlib.Path) -> str:
    text = path.read_text(encoding="utf-8")
    parts = text.split("---\n")
    return parts[2] if len(parts) > 2 else text


def score_text(text: str) -> dict:
    words = len(text.split())
    hits: dict[str, list[str]] = {k: [] for k in NAMED}
    distinct: set[str] = set()
    named_mentions = 0

    # Longest term first, blanking each match, so an entity is never counted
    # twice (e.g. "Thunder" inside "Thunder Wave").
    terms = sorted(
        ((term, kind) for kind, vocab in NAMED.items() for term in vocab),
        key=lambda tk: -len(tk[0]),
    )
    working = text
    for term, kind in terms:
        pattern = r"(?<![\w-])" + re.escape(term) + r"(?![\w-])"
        found = re.findall(pattern, working)
        if not found:
            continue
        working = re.sub(pattern, "\u0000", working)
        hits[kind].append(f"{term}×{len(found)}")
        distinct.add(term)
        named_mentions += len(found)

    lowered = text.lower()
    generic_mentions = 0
    for term in GENERIC:
        generic_mentions += len(
            re.findall(r"(?<![\w-])" + re.escape(term) + r"(?![\w-])", lowered)
        )

    n_distinct = len(distinct)
    density = named_mentions / max(words, 1) * 100
    ratio = named_mentions / max(named_mentions + generic_mentions, 1)

    breadth_pts = min(45.0, n_distinct * 2.6)
    density_pts = min(35.0, density / 4.0 * 35.0)
    ratio_pts = min(20.0, ratio / 0.35 * 20.0)
    total = round(breadth_pts + density_pts + ratio_pts, 1)

    return {
        "words": words,
        "distinct": n_distinct,
        "named_mentions": named_mentions,
        "generic_mentions": generic_mentions,
        "density_per_100w": round(density, 2),
        "specificity": round(ratio, 3),
        "breadth_pts": round(breadth_pts, 1),
        "density_pts": round(density_pts, 1),
        "ratio_pts": round(ratio_pts, 1),
        "score": min(100.0, total),
        "hits": {k: sorted(v) for k, v in hits.items() if v},
    }


def all_scores() -> list[dict]:
    rows = []
    for path in sorted((ROOT / "answers" / "pokemon").glob("*.md")):
        qid, slug = path.stem.split("-", 1)
        r = score_text(body_of(path))
        r.update({"id": qid, "slug": slug})
        rows.append(r)
    return rows


def band(s: float) -> str:
    if s >= 80: return "excellent"
    if s >= 65: return "strong"
    if s >= 50: return "adequate"
    if s >= 35: return "thin"
    return "generic"


def write_ledger(rows: list[dict]) -> None:
    rows_sorted = sorted(rows, key=lambda r: r["score"])
    avg = sum(r["score"] for r in rows) / len(rows)
    med = sorted(r["score"] for r in rows)[len(rows) // 2]

    out = ["# Pokémon-ness ledger", "",
           "How much each Pokémon answer actually leans on **named** Pokémon entities —",
           "real species, moves, items, abilities, characters, places — rather than generic",
           "furniture (\"a Trainer\", \"a Gym\", \"a battle\"). Generic terms are the denominator,",
           "not the numerator.", "",
           "Regenerate with `python3 scripts/pokemon_score.py`. Scoring is deterministic, so",
           "the diff between two commits of this file is the change in Pokémon-ness.", "",
           "```", "score = breadth (0-45) + density (0-35) + specificity (0-20)",
           "  breadth      distinct named entities used",
           "  density      named-entity mentions per 100 words",
           "  specificity  named / (named + generic) mentions", "```", "",
           f"**{len(rows)} answers · mean {avg:.1f} · median {med:.1f} · "
           f"min {rows_sorted[0]['score']:.1f} ({rows_sorted[0]['id']}) · "
           f"max {rows_sorted[-1]['score']:.1f} ({rows_sorted[-1]['id']})**", ""]

    dist = {}
    for r in rows:
        dist[band(r["score"])] = dist.get(band(r["score"]), 0) + 1
    out.append("| band | range | answers |")
    out.append("| --- | --- | --- |")
    for b, rng in [("excellent", "80-100"), ("strong", "65-79"), ("adequate", "50-64"),
                   ("thin", "35-49"), ("generic", "0-34")]:
        out.append(f"| {b} | {rng} | {dist.get(b, 0)} |")
    out += ["", "## Every answer, lowest first", "",
            "| score | band | id | answer | distinct | named | generic | per 100w |",
            "| ---: | --- | --- | --- | ---: | ---: | ---: | ---: |"]
    for r in rows_sorted:
        out.append(
            f"| **{r['score']:.1f}** | {band(r['score'])} | "
            f"[`{r['id']}`](answers/pokemon/{r['id']}-{r['slug']}.md) | {r['slug']} | "
            f"{r['distinct']} | {r['named_mentions']} | {r['generic_mentions']} | "
            f"{r['density_per_100w']:.1f} |")
    out.append("")
    (ROOT / "LEDGER.md").write_text("\n".join(out) + "\n", encoding="utf-8")


def main() -> int:
    args = sys.argv[1:]
    if args and args[0] == "--detail":
        qid = args[1]
        path = next((ROOT / "answers" / "pokemon").glob(f"{qid}-*.md"))
        r = score_text(body_of(path))
        print(json.dumps({k: v for k, v in r.items()}, indent=2, ensure_ascii=False))
        return 0
    rows = all_scores()
    if args and args[0] == "--json":
        print(json.dumps(rows, indent=2, ensure_ascii=False))
        return 0
    write_ledger(rows)
    avg = sum(r["score"] for r in rows) / len(rows)
    print(f"{len(rows)} answers scored · mean {avg:.1f}")
    print("\nlowest 15:")
    for r in sorted(rows, key=lambda x: x["score"])[:15]:
        print(f"  {r['score']:5.1f}  {r['id']}  {r['slug']:<38} "
              f"distinct={r['distinct']:<3} named={r['named_mentions']:<3} generic={r['generic_mentions']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
