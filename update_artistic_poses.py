import json

with open('cards.json', 'r', encoding='utf-8') as f:
    cards_data = json.load(f)

# Define unique artistic poses for Major Arcana and archetypes
artistic_poses = {
    "00-fool": "playful contrapposto standing on the infinity pool edge on tiptoes, one foot poised over the water, holding a white rose up with a breezy head-tilt and charming wink",
    "01-magician": "commanding standing stance with one hand pointed toward the heavens channeling lightning and the other gesturing downward over floating elemental relics",
    "02-priestess": "poised statuesque standing pose between two illuminated pillars, one hand delicately holding a glowing holographic tablet, feet gracefully dipped in shallow water",
    "03-empress": "sensual reclining pose reclining back against a curved velvet-cushioned poolside lounge, one arm draped behind head and legs crossed elegantly in warm water",
    "04-emperor": "powerful seated-to-standing stride emerging from a volcanic thermal bath, hands holding twin golden scepters, chest upright with commanding posture",
    "05-hierophant": "dignified walking pose stepping gracefully through crystal bath water, holding twin triple-cross scepters raised symmetrically, serene upright spine",
    "06-lovers": "romantic contrapposto stance standing waist-deep in pink rose-water pool, hands clasped gently near heart, head tilted back softly with dreamy lovestruck gaze",
    "07-chariot": "dynamic athletic forward stride walking out of the hydro-chamber with hands on hips, confident hip sway, head held high with wind-swept ponytail",
    "08-strength": "tender contrapposto leaning gently against a golden lion fountain, one hand softly caressing the lion's mane, smiling warmly with relaxed arched back",
    "09-hermit": "quiet introspective standing pose on wet stone beside steaming onsen, holding a golden lantern up high at eye level to illuminate the snowy twilight",
    "10-wheel": "dynamic center-stage walking pose turning towards viewer, hip accentuated with hand resting near thigh, walking through shallow pool beneath glowing zodiac wheel",
    "11-justice": "flawless symmetrical standing pose, right hand holding upright crystal sword aloft, left hand extending golden balance scales steadily at shoulder height",
    "12-hanged": "graceful floating pose suspended weightlessly horizontally in a zero-gravity flotation pool, arms drifted outward, legs crossed in an elegant figure-4 shape",
    "13-death": "alluring over-the-shoulder seated pose on the edge of a black obsidian pool, glancing back with seductive fatal eyes, one hand dipping into dark water with white roses",
    "14-temperance": "ethereal flowing stance standing at the foot of an indoor waterfall, holding two crystal chalices pouring glowing streams of water back and forth in mid-air",
    "15-devil": "provocative seated pose sitting on the marble jacuzzi ledge, knees slightly apart with feet dipping in hot red water, leaning back on both palms with arched spine",
    "16-tower": "dramatic dynamic motion pose on wet glass deck, body twisting dynamically as lightning flashes, one hand raised to hair, hair whipping wildly in wind",
    "17-the-star": "kneeling on one knee at the edge of an infinity pool under the giant eight-pointed star, pouring glowing water from two golden urns into pool and earth",
    "18-moon": "alluring standing contrapposto shower pose under a cascading glass rain shower, one hand lifting wet hair from nape, head tilted back, water running down curves",
    "19-sun": "radiant sunbathing standing pose with arms outstretched toward golden sunbeams, chest lifted in ecstasy, beaming joyfully with water droplets glistening in sunlight",
    "20-judgement": "divine ascending pose standing on tiptoes on shallow water, arms opened wide to heaven, head tilted upward greeting radiant golden light rays of awakening",
    "21-world": "goddess victory pose standing at center of a glowing circular portal ring, holding two golden wands gracefully, triumphant and radiant in 360-degree city view"
}

# Update cards with specific pose and regenerate master prompt
for c in cards_data['cards']:
    slug = c['slug']
    group = c['group']
    title = c['title']
    
    pose = artistic_poses.get(slug)
    if not pose:
        if group == 'wands':
            pose = "dynamic energetic stance with one hand raising a glowing flame wand and body turned in an active contrapposto curve"
        elif group == 'cups':
            pose = "graceful fluid stance gently wading through warm water, one hand cupping a glowing chalice and head tilted with soft sensual smile"
        elif group == 'swords':
            pose = "sharp poised stance with sleek posture, holding a gleaming crystal blade with sharp cat-eye gaze directed at viewer"
        elif group == 'pentacles':
            pose = "luxurious relaxed stance lounging on warm marble poolside with one hand presenting a glowing golden pentacle coin"
        else:
            pose = "alluring standing contrapposto pose with arched spine and weight shifted to one leg, emphasizing feminine silhouette"
            
    c['artistic_pose'] = pose
    
    hair_desc = c.get('hair_style', c.get('hair', 'silky hair'))
    eyes_desc = c.get('eyes_style', c.get('eyes', 'alluring cat eyes'))
    expr_desc = c.get('expression_style', 'seductive smile, blushing cheeks')
    bikini_color = c.get('bikini_color', 'sheer translucent chiffon')
    bikini_style = c.get('bikini_style', 'micro-string bikini')
    scene_theme = c.get('scene', 'luxury ambient setting')
    
    c['master_prompt'] = f"""A vertical Korean adult webtoon illustration in manhwa art style matching Capture3.PNG.
COMPLETELY FRAMELESS: no decorative borders, no card frames, no banner ribbon, edge-to-edge illustration. Only the clean title text '{title}' in elegant antique gold lettering centered at the bottom (NO numbers, NO Roman numerals).

Character & Pose: An alluring, voluptuous young woman ({c.get('age', '20 years old')}), {c.get('build', 'slender waist with curvy feminine silhouette')}, with {hair_desc}, {eyes_desc}, {expr_desc}. Artistic Pose: {pose}. She has glowing porcelain skin with glossy specular wet highlights and glistening water droplets.
Outfit: Wearing a form-fitting wet {bikini_color} {bikini_style} hugging her figure tightly, emphasizing bust contours, narrow waist, and rosy glowing skin highlights through the wet translucent fabric, barefoot with completely bare feet and legs.

Scene & Atmosphere: {scene_theme}.
Tarot Symbolism: {c['emblem']} integrated naturally into the modern luxury environment with glowing ambient lighting.
{c['count_lock']}

High-gloss specular wet skin highlights, crisp webtoon lineart, cinematic ambient lighting, masterpiece manhwa illustration.

NEGATIVE: numbers, roman numerals, borders, frames, banner, ribbon, margin, outer box, shoes, boots, sandals, socks, heavy clothes, casual street clothes, deformed hands, extra limbs, bad anatomy, low quality, watermark, signature."""

with open('cards.json', 'w', encoding='utf-8') as f:
    json.dump(cards_data, f, ensure_ascii=False, indent=2)

print("Updated cards.json with unique artistic poses for all cards!")
