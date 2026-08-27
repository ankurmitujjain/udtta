import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

output_dir = r"c:\Users\ankur\OneDrive - Yash Technologies Pvt Ltd\Desktop\Customer\Portfolio\tt\UDTTA\graphics"
os.makedirs(output_dir, exist_ok=True)

logo_path = r"c:\Users\ankur\OneDrive - Yash Technologies Pvt Ltd\Desktop\Customer\Portfolio\tt\UDTTA\UDTTA_Logo_Circular.png"
logo = Image.open(logo_path).convert("RGBA")

# 1. Save standard Left Chest & Right Sleeve badges
logo_chest = logo.resize((1050, 1050), Image.Resampling.LANCZOS)
logo_chest.save(os.path.join(output_dir, "UDTTA_Chest_Emblem_300DPI.png"), dpi=(300, 300))

logo_sleeve = logo.resize((900, 900), Image.Resampling.LANCZOS)
logo_sleeve.save(os.path.join(output_dir, "UDTTA_Sleeve_Emblem_300DPI.png"), dpi=(300, 300))
print("Saved Chest & Sleeve Badges (300 DPI).")

# Helpers for arched text and sports block numbers
def draw_arched_text(draw, text, center_x, center_y, radius, start_angle_deg, end_angle_deg, font, fill_color, outline_color=None, outline_width=0):
    n = len(text)
    if n == 1:
        angles = [(start_angle_deg + end_angle_deg) / 2]
    else:
        step = (end_angle_deg - start_angle_deg) / (n - 1)
        angles = [start_angle_deg + i * step for i in range(n)]
    
    for char, angle in zip(text, angles):
        rad = math.radians(angle)
        # Position on arch
        cx = center_x + radius * math.sin(rad)
        cy = center_y - radius * math.cos(rad)
        
        # Create a small transparent image for the character to rotate
        char_img = Image.new("RGBA", (300, 300), (0, 0, 0, 0))
        char_draw = ImageDraw.Draw(char_img)
        
        bbox = font.getbbox(char)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        x0 = (300 - w) / 2 - bbox[0]
        y0 = (300 - h) / 2 - bbox[1]
        
        if outline_color and outline_width > 0:
            for dx in range(-outline_width, outline_width + 1):
                for dy in range(-outline_width, outline_width + 1):
                    if dx * dx + dy * dy <= outline_width * outline_width:
                        char_draw.text((x0 + dx, y0 + dy), char, font=font, fill=outline_color)
        
        char_draw.text((x0, y0), char, font=font, fill=fill_color)
        
        # Rotate character to align tangent to arch
        rot_img = char_img.rotate(-angle, resample=Image.Resampling.BICUBIC, expand=True)
        rx = int(cx - rot_img.width / 2)
        ry = int(cy - rot_img.height / 2)
        draw._image.alpha_composite(rot_img, (rx, ry))

def create_back_print(player_name, player_num, outline_color="#FFB800", filename="back_print.png"):
    W, H = 2400, 2800
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    impact_large = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 260)
    impact_name = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 230)
    impact_num = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 780)
    
    # 1. Arched UJJAIN
    draw_arched_text(draw, "UJJAIN", W // 2, 850, 520, -38, 38, impact_large, "#FFFFFF", outline_color, 8)
    
    # 2. Player Name (e.g. SHARMA)
    bbox_name = impact_name.getbbox(player_name)
    nw = bbox_name[2] - bbox_name[0]
    nx = (W - nw) // 2
    ny = 680
    
    # Outline for name
    for dx in range(-7, 8):
        for dy in range(-7, 8):
            if dx*dx + dy*dy <= 49:
                draw.text((nx + dx, ny + dy), player_name, font=impact_name, fill=outline_color)
    draw.text((nx, ny), player_name, font=impact_name, fill="#FFFFFF")
    
    # 3. Jersey Number (e.g. 07)
    bbox_num = impact_num.getbbox(player_num)
    num_w = bbox_num[2] - bbox_num[0]
    num_x = (W - num_w) // 2
    num_y = 1020
    
    for dx in range(-14, 15):
        for dy in range(-14, 15):
            if dx*dx + dy*dy <= 196:
                draw.text((num_x + dx, num_y + dy), player_num, font=impact_num, fill=outline_color)
    draw.text((num_x, num_y), player_num, font=impact_num, fill="#FFFFFF")
    
    img.save(os.path.join(output_dir, filename), dpi=(300, 300))
    print(f"Saved {filename}")
    return img

# Generate all back prints
create_back_print("SHARMA", "07", outline_color="#FFB800", filename="P4_Back_Print_SHARMA_07_300DPI.png")
create_back_print("SHARMA", "07", outline_color="#FFB800", filename="P5_Back_Print_SHARMA_07_300DPI.png")
create_back_print("SINGH", "11", outline_color="#FFB800", filename="P6_Back_Print_SINGH_11_300DPI.png")
create_back_print("MEHTA", "14", outline_color="#FFB800", filename="P7_Back_Print_MEHTA_14_300DPI.png")
create_back_print("GUPTA", "18", outline_color="#FFB800", filename="P8_Back_Print_GUPTA_18_300DPI.png")

# 2. Front Artwork Graphics Generation
def create_p4_flame_artwork():
    W, H = 2800, 2200
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw flame tongues (Red outer, Yellow inner, Gold core)
    # Layer 1: Crimson Red Flames
    red_flames = [
        [(200, H), (250, 1400), (350, 900), (450, 1300), (600, 700), (750, 1100), (950, 400), (1100, 950), (1300, 300), (1500, 900), (1700, 500), (1850, 1050), (2050, 750), (2200, 1200), (2400, 950), (2550, 1500), (2600, H)]
    ]
    for pts in red_flames:
        draw.polygon(pts, fill=(230, 57, 70, 255))
        
    # Layer 2: Vibrant Golden Yellow Flames
    yellow_flames = [
        [(300, H), (380, 1500), (450, 1100), (550, 1450), (680, 950), (820, 1300), (1020, 650), (1180, 1150), (1340, 550), (1520, 1100), (1720, 750), (1880, 1250), (2060, 980), (2220, 1380), (2380, 1150), (2480, 1650), (2500, H)]
    ]
    for pts in yellow_flames:
        draw.polygon(pts, fill=(255, 184, 0, 255))
        
    # Layer 3: Bright Lemon Core Flames
    core_flames = [
        [(400, H), (500, 1600), (600, 1300), (750, 1550), (900, 1150), (1050, 1450), (1200, 900), (1360, 1350), (1540, 800), (1700, 1300), (1880, 1050), (2040, 1450), (2200, 1250), (2340, 1700), (2400, H)]
    ]
    for pts in core_flames:
        draw.polygon(pts, fill=(255, 230, 102, 255))

    img.save(os.path.join(output_dir, "P4_Solar_Flare_Front_Artwork_300DPI.png"), dpi=(300, 300))
    print("Saved P4_Solar_Flare_Front_Artwork_300DPI.png")

def create_p5_carbon_flame_artwork():
    W, H = 2800, 2200
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Golden flame palette on carbon black
    red_flames = [
        [(200, H), (250, 1400), (350, 900), (450, 1300), (600, 700), (750, 1100), (950, 400), (1100, 950), (1300, 300), (1500, 900), (1700, 500), (1850, 1050), (2050, 750), (2200, 1200), (2400, 950), (2550, 1500), (2600, H)]
    ]
    for pts in red_flames:
        draw.polygon(pts, fill=(230, 138, 0, 255))
        
    yellow_flames = [
        [(300, H), (380, 1500), (450, 1100), (550, 1450), (680, 950), (820, 1300), (1020, 650), (1180, 1150), (1340, 550), (1520, 1100), (1720, 750), (1880, 1250), (2060, 980), (2220, 1380), (2380, 1150), (2480, 1650), (2500, H)]
    ]
    for pts in yellow_flames:
        draw.polygon(pts, fill=(255, 184, 0, 255))
        
    core_flames = [
        [(400, H), (500, 1600), (600, 1300), (750, 1550), (900, 1150), (1050, 1450), (1200, 900), (1360, 1350), (1540, 800), (1700, 1300), (1880, 1050), (2040, 1450), (2200, 1250), (2340, 1700), (2400, H)]
    ]
    for pts in core_flames:
        draw.polygon(pts, fill=(255, 240, 150, 255))

    img.save(os.path.join(output_dir, "P5_Carbon_Flame_Front_Artwork_300DPI.png"), dpi=(300, 300))
    print("Saved P5_Carbon_Flame_Front_Artwork_300DPI.png")

def create_p6_aero_wave_artwork():
    W, H = 2800, 2400
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Smooth aerodynamic spin wave arcs (Gold & Cyan ribbons)
    # Wave 1: Cyan ribbon flowing from top right / shoulder down to bottom left
    for offset, alpha in [(0, 255), (15, 200), (30, 150)]:
        pts_cyan = [
            (2600, 200), (2200, 450), (1700, 900), (1200, 1500), (800, 2000), (400, 2350),
            (200, 2400), (150, 2400), (350, 2250), (700, 1850), (1100, 1350), (1600, 750), (2100, 350), (2550, 120)
        ]
        draw.polygon(pts_cyan, fill=(6, 182, 212, alpha))
        
    # Wave 2: Gold ribbon interwoven
    pts_gold = [
        (2750, 350), (2350, 600), (1850, 1050), (1350, 1650), (950, 2150), (550, 2400),
        (350, 2400), (500, 2300), (850, 1950), (1250, 1450), (1750, 850), (2250, 450), (2700, 220)
    ]
    draw.polygon(pts_gold, fill=(255, 184, 0, 255))
    
    # Wave 3: Secondary electric cyan swoosh
    pts_cyan2 = [
        (2400, 700), (1950, 1200), (1450, 1800), (1050, 2300), (800, 2400),
        (650, 2400), (900, 2200), (1300, 1650), (1800, 1050), (2300, 550)
    ]
    draw.polygon(pts_cyan2, fill=(56, 189, 248, 255))

    # Wave 4: Gold accent swoop on left hip
    pts_gold2 = [
        (200, 800), (500, 1300), (900, 1850), (1400, 2350), (1600, 2400),
        (1450, 2400), (800, 1750), (400, 1200), (150, 750)
    ]
    draw.polygon(pts_gold2, fill=(255, 184, 0, 230))

    img.save(os.path.join(output_dir, "P6_Aero_Wave_Front_Artwork_300DPI.png"), dpi=(300, 300))
    print("Saved P6_Aero_Wave_Front_Artwork_300DPI.png")

def create_p7_hex_matrix_artwork():
    W, H = 2800, 2400
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Hexagon grid generator for side flanks & bottom
    def draw_hexagon(center_x, center_y, size, fill, outline=None):
        pts = []
        for i in range(6):
            angle_deg = 60 * i - 30
            rad = math.radians(angle_deg)
            pts.append((center_x + size * math.cos(rad), center_y + size * math.sin(rad)))
        draw.polygon(pts, fill=fill, outline=outline)

    # Left flank & right flank hex clusters with gradient density
    hex_size = 55
    dx = hex_size * math.sqrt(3)
    dy = hex_size * 1.5
    
    # Flank bounding columns
    for row in range(12, 28):
        y = row * dy
        for col in range(0, 10):
            x = col * dx + ((row % 2) * (dx / 2))
            # Alpha gradient from bottom to top
            alpha = int(max(0, min(255, (y - 800) / 1400 * 255)))
            if alpha > 10:
                gold_alpha = int(alpha * 0.8)
                blue_fill = (30, 58, 138, int(alpha * 0.65))
                gold_outline = (255, 184, 0, gold_alpha)
                draw_hexagon(x, y, hex_size, fill=blue_fill, outline=gold_outline)
                
        # Right flank
        for col in range(18, 28):
            x = col * dx + ((row % 2) * (dx / 2))
            alpha = int(max(0, min(255, (y - 800) / 1400 * 255)))
            if alpha > 10:
                gold_alpha = int(alpha * 0.8)
                blue_fill = (30, 58, 138, int(alpha * 0.65))
                gold_outline = (255, 184, 0, gold_alpha)
                draw_hexagon(x, y, hex_size, fill=blue_fill, outline=gold_outline)

    # Dynamic athletic flank accent lines (Gold pinstripes)
    draw.line([(580, 600), (520, 2400)], fill=(255, 184, 0, 255), width=18)
    draw.line([(620, 700), (560, 2400)], fill=(30, 58, 138, 255), width=12)
    
    draw.line([(2220, 600), (2280, 2400)], fill=(255, 184, 0, 255), width=18)
    draw.line([(2180, 700), (2240, 2400)], fill=(30, 58, 138, 255), width=12)

    img.save(os.path.join(output_dir, "P7_Hex_Matrix_Front_Artwork_300DPI.png"), dpi=(300, 300))
    print("Saved P7_Hex_Matrix_Front_Artwork_300DPI.png")

def create_p8_speed_block_artwork():
    W, H = 2800, 2400
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Sharp diagonal tournament racing speed blocks & chevron arrows
    # Diagonal angle ~ -35 degrees
    # Main broad crimson band
    pts_crimson = [
        (0, 1750), (2800, 650), (2800, 1150), (0, 2250)
    ]
    draw.polygon(pts_crimson, fill=(230, 57, 70, 255))
    
    # Royal athletic blue band
    pts_royal = [
        (0, 2050), (2800, 950), (2800, 1450), (0, 2400), (0, 2400)
    ]
    draw.polygon(pts_royal, fill=(30, 58, 138, 255))
    
    # Gold accent pinstripes
    draw.line([(0, 1730), (2800, 630)], fill=(255, 184, 0, 255), width=22)
    draw.line([(0, 2030), (2800, 930)], fill=(255, 184, 0, 255), width=16)
    draw.line([(0, 2380), (2800, 1430)], fill=(255, 184, 0, 255), width=18)
    
    # Speed Chevron series across upper section of the block
    for i in range(10):
        cx = 350 + i * 220
        cy = 1500 - i * 85
        ch_pts = [
            (cx, cy), (cx + 90, cy - 35), (cx + 120, cy - 35), (cx + 30, cy), (cx + 120, cy + 35), (cx + 90, cy + 35)
        ]
        draw.polygon(ch_pts, fill=(255, 184, 0, 240))

    img.save(os.path.join(output_dir, "P8_Speed_Block_Front_Artwork_300DPI.png"), dpi=(300, 300))
    print("Saved P8_Speed_Block_Front_Artwork_300DPI.png")

create_p4_flame_artwork()
create_p5_carbon_flame_artwork()
create_p6_aero_wave_artwork()
create_p7_hex_matrix_artwork()
create_p8_speed_block_artwork()

# 3. Create Full Manufacturer Print Pack Sheets (A3/Poster Specification Sheet)
def create_print_pack_sheet(option_id, option_title, jersey_color, front_art_name, back_art_name, player_name, num_str, filename):
    W, H = 3500, 2400
    sheet = Image.new("RGBA", (W, H), (15, 23, 42, 255))
    draw = ImageDraw.Draw(sheet)
    
    font_title = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 85)
    font_sub = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 48)
    font_section = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 60)
    font_spec = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 36)
    font_tag = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 32)
    
    # Header Banner
    draw.rectangle([(0, 0), (W, 190)], fill=(10, 25, 47, 255))
    draw.line([(0, 190), (W, 190)], fill=(255, 184, 0, 255), width=6)
    
    draw.text((60, 40), f"UDTTA MASTER APPAREL PRINT SPECIFICATION: {option_id} - {option_title}", font=font_title, fill="#FFB800")
    draw.text((60, 130), f"Garment: 100% Synthetic Polyester Performance Polo • Colorway: {jersey_color} • Print Process: Dye Sublimation / DTF (300 DPI)", font=font_sub, fill="#94A3B8")
    
    # 4 Quadrants:
    # Top Left: Front Torso Sublimation Art
    # Top Right: Back Print (UJJAIN + Name + No)
    # Bottom Left: Left Chest & Right Sleeve Badges
    # Bottom Right: Specifications & Printing Instructions
    
    # Box 1: Front Sublimation
    draw.rounded_rectangle([(60, 240), (1650, 1450)], radius=24, fill=(11, 34, 64, 200), outline=(255, 184, 0, 100), width=3)
    draw.text((90, 270), "1. FRONT TORSO SUBLIMATION ARTWORK", font=font_section, fill="#FFB800")
    draw.text((90, 340), "Print Size: 14\" x 18\" (Full Width Hem Wrap) • Process: 4-Color Dye Sublimation", font=font_spec, fill="#E2E8F0")
    
    front_art = Image.open(os.path.join(output_dir, front_art_name)).convert("RGBA")
    front_art_thumb = front_art.resize((1400, 950), Image.Resampling.LANCZOS)
    sheet.alpha_composite(front_art_thumb, (120, 420))
    
    # Box 2: Back Print
    draw.rounded_rectangle([(1750, 240), (3440, 1450)], radius=24, fill=(11, 34, 64, 200), outline=(255, 184, 0, 100), width=3)
    draw.text((1780, 270), f"2. BACK NAME & NUMBER PRINT ({player_name} #{num_str})", font=font_section, fill="#FFB800")
    draw.text((1780, 340), "Print Size: 12\" x 16\" Upper Back Center • Font: Athletic Block with 4mm Stroke", font=font_spec, fill="#E2E8F0")
    
    back_art = Image.open(os.path.join(output_dir, back_art_name)).convert("RGBA")
    back_art_thumb = back_art.resize((850, 990), Image.Resampling.LANCZOS)
    sheet.alpha_composite(back_art_thumb, (2150, 410))
    
    # Box 3: Badges (Left Chest & Right Sleeve)
    draw.rounded_rectangle([(60, 1520), (1650, 2320)], radius=24, fill=(11, 34, 64, 200), outline=(255, 184, 0, 100), width=3)
    draw.text((90, 1550), "3. ASSOCIATION EMBLEM BADGES", font=font_section, fill="#FFB800")
    
    # Chest Badge
    chest_badge = Image.open(os.path.join(output_dir, "UDTTA_Chest_Emblem_300DPI.png")).convert("RGBA")
    cb_thumb = chest_badge.resize((550, 550), Image.Resampling.LANCZOS)
    sheet.alpha_composite(cb_thumb, (120, 1680))
    draw.text((150, 1630), "LEFT CHEST (3.5\" x 3.5\")", font=font_spec, fill="#38BDF8")
    
    # Sleeve Badge
    sleeve_badge = Image.open(os.path.join(output_dir, "UDTTA_Sleeve_Emblem_300DPI.png")).convert("RGBA")
    sb_thumb = sleeve_badge.resize((480, 480), Image.Resampling.LANCZOS)
    sheet.alpha_composite(sb_thumb, (850, 1720))
    draw.text((880, 1630), "RIGHT SLEEVE (3.0\" x 3.0\")", font=font_spec, fill="#38BDF8")
    
    # Box 4: Technical Print Specs
    draw.rounded_rectangle([(1750, 1520), (3440, 2320)], radius=24, fill=(11, 34, 64, 200), outline=(255, 184, 0, 100), width=3)
    draw.text((1780, 1550), "4. PRODUCTION & COLORWAY SPECIFICATIONS", font=font_section, fill="#FFB800")
    
    specs = [
        ("Base Garment", "100% Micro-Mesh Quick-Dry Polyester (160 GSM)"),
        ("Collar Construction", "Structured Knitted Collar with Gold Tipping & 2 Buttons"),
        ("Chest Badge Placement", "Left Chest: 7.5 cm down from shoulder seam, centered on breast"),
        ("Sleeve Badge Placement", "Right Sleeve: Centered 4 cm above the ribbed cuff"),
        ("Sublimation Heat Settings", "200°C (392°F) for 35-40 seconds at medium-high pressure"),
        ("Dye Sub Color Calibration", "Navy #0A192F | Black #111115 | Gold #FFB800 | Crimson #E63946")
    ]
    
    y_pos = 1640
    for label, val in specs:
        draw.text((1780, y_pos), f"• {label}:", font=font_spec, fill="#FFD166")
        draw.text((2280, y_pos), val, font=font_spec, fill="#F8FAFC")
        y_pos += 85
        
    sheet.save(os.path.join(output_dir, filename), dpi=(300, 300))
    print(f"Saved Complete Print Pack Sheet: {filename}")

create_print_pack_sheet("Option P4", "Solar Flare Collared Polo (Navy)", "Deep Navy Blue (#0A192F)", "P4_Solar_Flare_Front_Artwork_300DPI.png", "P4_Back_Print_SHARMA_07_300DPI.png", "SHARMA", "07", "P4_Full_Print_Bundle_300DPI.png")
create_print_pack_sheet("Option P5", "Carbon Flame Collared Polo (Black)", "Stealth Carbon Black (#111115)", "P5_Carbon_Flame_Front_Artwork_300DPI.png", "P5_Back_Print_SHARMA_07_300DPI.png", "SHARMA", "07", "P5_Full_Print_Bundle_300DPI.png")
create_print_pack_sheet("Option P6", "Donic Aero-Wave Spin Polo (Navy)", "Deep Navy Blue (#0A192F)", "P6_Aero_Wave_Front_Artwork_300DPI.png", "P6_Back_Print_SINGH_11_300DPI.png", "SINGH", "11", "P6_Full_Print_Bundle_300DPI.png")
create_print_pack_sheet("Option P7", "Butterfly Hex-Matrix Polo (Black)", "Stealth Carbon Black (#111115)", "P7_Hex_Matrix_Front_Artwork_300DPI.png", "P7_Back_Print_MEHTA_14_300DPI.png", "MEHTA", "14", "P7_Full_Print_Bundle_300DPI.png")
create_print_pack_sheet("Option P8", "Tibhar Speed-Block Polo (Navy)", "Deep Navy Blue (#0A192F)", "P8_Speed_Block_Front_Artwork_300DPI.png", "P8_Back_Print_GUPTA_18_300DPI.png", "GUPTA", "18", "P8_Full_Print_Bundle_300DPI.png")
create_print_pack_sheet("Option P9", "Cyber-Stream Athletic V-Neck", "Royal Blue & Navy (#1E3A8A / #0A192F)", "P9_Cyber_Stream_Front_Artwork_300DPI.png", "P9_Back_Print_JOSHI_21_300DPI.png", "JOSHI", "21", "P9_Full_Print_Bundle_300DPI.png")
create_print_pack_sheet("Option P10", "Prism-Grid Facet V-Neck", "Dark Slate Charcoal (#252930)", "P10_Prism_Grid_Front_Artwork_300DPI.png", "P10_Back_Print_PATEL_23_300DPI.png", "PATEL", "23", "P10_Full_Print_Bundle_300DPI.png")

print("All production print graphics and bundles generated successfully!")
