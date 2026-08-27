import os
import math
import shutil
from PIL import Image, ImageDraw, ImageFont, ImageFilter

output_dir = r"c:\Users\ankur\OneDrive - Yash Technologies Pvt Ltd\Desktop\Customer\Portfolio\tt\UDTTA\graphics"
os.makedirs(output_dir, exist_ok=True)

workspace_dir = r"c:\Users\ankur\OneDrive - Yash Technologies Pvt Ltd\Desktop\Customer\Portfolio\tt\UDTTA"

# Copy new P4 Aarav polo image to workspace
p4_generated_src = r"C:\Users\ankur\.gemini\antigravity-ide\brain\f7b8f0f5-3f28-4049-b9f9-dfb3cf31b45a\player_p4_aarav_polo_1787812256902.jpg"
if os.path.exists(p4_generated_src):
    shutil.copyfile(p4_generated_src, os.path.join(workspace_dir, "UDTTA_Player_P4_Navy_Polo.jpg"))
    print("Copied updated P4 Aarav Polo to workspace.")

logo_path = os.path.join(workspace_dir, "UDTTA_Logo_Circular.png")
logo = Image.open(logo_path).convert("RGBA")

# 1. Standard Badges
logo_chest = logo.resize((1050, 1050), Image.Resampling.LANCZOS)
logo_chest.save(os.path.join(output_dir, "UDTTA_Chest_Emblem_300DPI.png"), dpi=(300, 300))

logo_sleeve = logo.resize((900, 900), Image.Resampling.LANCZOS)
logo_sleeve.save(os.path.join(output_dir, "UDTTA_Sleeve_Emblem_300DPI.png"), dpi=(300, 300))
print("Saved Chest & Sleeve Badges.")

# Arched text helper
def draw_arched_text(draw, text, center_x, center_y, radius, start_angle_deg, end_angle_deg, font, fill_color, outline_color=None, outline_width=0):
    n = len(text)
    if n == 1:
        angles = [(start_angle_deg + end_angle_deg) / 2]
    else:
        step = (end_angle_deg - start_angle_deg) / (n - 1)
        angles = [start_angle_deg + i * step for i in range(n)]
    
    for char, angle in zip(text, angles):
        rad = math.radians(angle)
        cx = center_x + radius * math.sin(rad)
        cy = center_y - radius * math.cos(rad)
        
        char_img = Image.new("RGBA", (320, 320), (0, 0, 0, 0))
        char_draw = ImageDraw.Draw(char_img)
        
        bbox = font.getbbox(char)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        x0 = (320 - w) / 2 - bbox[0]
        y0 = (320 - h) / 2 - bbox[1]
        
        if outline_color and outline_width > 0:
            for dx in range(-outline_width, outline_width + 1):
                for dy in range(-outline_width, outline_width + 1):
                    if dx * dx + dy * dy <= outline_width * outline_width:
                        char_draw.text((x0 + dx, y0 + dy), char, font=font, fill=outline_color)
        
        char_draw.text((x0, y0), char, font=font, fill=fill_color)
        rot_img = char_img.rotate(-angle, resample=Image.Resampling.BICUBIC, expand=True)
        rx = int(cx - rot_img.width / 2)
        ry = int(cy - rot_img.height / 2)
        draw._image.alpha_composite(rot_img, (rx, ry))

# Back typography generator
def create_back_print(player_name, player_num, outline_color="#FFB800", filename="back_print.png"):
    W, H = 2400, 2800
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    impact_large = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 260)
    impact_name = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 230)
    impact_num = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 780)
    
    draw_arched_text(draw, "UJJAIN", W // 2, 850, 520, -38, 38, impact_large, "#FFFFFF", outline_color, 8)
    
    bbox_name = impact_name.getbbox(player_name)
    nw = bbox_name[2] - bbox_name[0]
    nx = (W - nw) // 2
    ny = 680
    
    for dx in range(-7, 8):
        for dy in range(-7, 8):
            if dx*dx + dy*dy <= 49:
                draw.text((nx + dx, ny + dy), player_name, font=impact_name, fill=outline_color)
    draw.text((nx, ny), player_name, font=impact_name, fill="#FFFFFF")
    
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

# Generate all back prints for P1 - P10
create_back_print("SHARMA", "07", outline_color="#FFB800", filename="P1_Back_Print_SHARMA_07_300DPI.png")
create_back_print("SHARMA", "07", outline_color="#FFB800", filename="P2_Back_Print_SHARMA_07_300DPI.png")
create_back_print("VERMA", "10", outline_color="#1E3A8A", filename="P3_Back_Print_VERMA_10_300DPI.png")
create_back_print("AARAV", "07", outline_color="#FFB800", filename="P4_Back_Print_AARAV_07_300DPI.png")
create_back_print("SHARMA", "07", outline_color="#FFB800", filename="P5_Back_Print_SHARMA_07_300DPI.png")
create_back_print("SINGH", "11", outline_color="#FFB800", filename="P6_Back_Print_SINGH_11_300DPI.png")
create_back_print("MEHTA", "14", outline_color="#FFB800", filename="P7_Back_Print_MEHTA_14_300DPI.png")
create_back_print("GUPTA", "18", outline_color="#FFB800", filename="P8_Back_Print_GUPTA_18_300DPI.png")
create_back_print("JOSHI", "21", outline_color="#FFB800", filename="P9_Back_Print_JOSHI_21_300DPI.png")
create_back_print("PATEL", "23", outline_color="#FFB800", filename="P10_Back_Print_PATEL_23_300DPI.png")

# 2. Front Artwork Generators
def create_flame_art(gold_mode=False, filename="flame.png"):
    W, H = 2800, 2200
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    if gold_mode:
        c1 = (230, 138, 0, 255)
        c2 = (255, 184, 0, 255)
        c3 = (255, 230, 120, 255)
    else:
        c1 = (230, 57, 70, 255)
        c2 = (255, 184, 0, 255)
        c3 = (255, 230, 102, 255)
        
    red_flames = [
        [(200, H), (250, 1400), (350, 900), (450, 1300), (600, 700), (750, 1100), (950, 400), (1100, 950), (1300, 300), (1500, 900), (1700, 500), (1850, 1050), (2050, 750), (2200, 1200), (2400, 950), (2550, 1500), (2600, H)]
    ]
    for pts in red_flames:
        draw.polygon(pts, fill=c1)
        
    yellow_flames = [
        [(300, H), (380, 1500), (450, 1100), (550, 1450), (680, 950), (820, 1300), (1020, 650), (1180, 1150), (1340, 550), (1520, 1100), (1720, 750), (1880, 1250), (2060, 980), (2220, 1380), (2380, 1150), (2480, 1650), (2500, H)]
    ]
    for pts in yellow_flames:
        draw.polygon(pts, fill=c2)
        
    core_flames = [
        [(400, H), (500, 1600), (600, 1300), (750, 1550), (900, 1150), (1050, 1450), (1200, 900), (1360, 1350), (1540, 800), (1700, 1300), (1880, 1050), (2040, 1450), (2200, 1250), (2340, 1700), (2400, H)]
    ]
    for pts in core_flames:
        draw.polygon(pts, fill=c3)

    img.save(os.path.join(output_dir, filename), dpi=(300, 300))
    print(f"Saved {filename}")

create_flame_art(gold_mode=False, filename="P1_Solar_Flare_Front_Artwork_300DPI.png")
create_flame_art(gold_mode=True, filename="P2_Carbon_Flame_Front_Artwork_300DPI.png")
create_flame_art(gold_mode=False, filename="P4_Solar_Flare_Front_Artwork_300DPI.png")
create_flame_art(gold_mode=True, filename="P5_Carbon_Flame_Front_Artwork_300DPI.png")

# P3 Speed Raglan Art
def create_p3_speed_raglan():
    W, H = 2800, 2200
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Dynamic aerodynamic velocity chevrons and speed swooshes
    for i in range(12):
        y_off = i * 150
        pts = [
            (100 + i*40, H - y_off),
            (600 + i*80, H - 400 - y_off),
            (1400 + i*60, H - 700 - y_off),
            (2400 + i*30, H - 850 - y_off),
            (2400 + i*30, H - 770 - y_off),
            (1400 + i*60, H - 620 - y_off),
            (600 + i*80, H - 320 - y_off),
            (100 + i*40, H - y_off + 80)
        ]
        alpha = int(255 - i * 16)
        col = (30, 58, 138, max(50, alpha)) if i % 2 == 0 else (255, 184, 0, max(50, alpha))
        draw.polygon(pts, fill=col)
        
    img.save(os.path.join(output_dir, "P3_Speed_Raglan_Front_Artwork_300DPI.png"), dpi=(300, 300))
    print("Saved P3_Speed_Raglan_Front_Artwork_300DPI.png")

create_p3_speed_raglan()

# P6 Aero-Wave
def create_p6_wave_artwork():
    W, H = 2800, 2200
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    for i in range(8):
        points = []
        for x in range(0, W + 50, 40):
            y = int(H - 400 - i * 130 + math.sin((x / W) * 2 * math.pi + i * 0.4) * 350 - (x / W) * 300)
            points.append((x, y))
        
        color = (255, 184, 0, 240) if i % 2 == 0 else (6, 182, 212, 230)
        thick = 45 - i * 3
        draw.line(points, fill=color, width=thick, joint="curve")
        
    img.save(os.path.join(output_dir, "P6_Aero_Wave_Front_Artwork_300DPI.png"), dpi=(300, 300))
    print("Saved P6_Aero_Wave_Front_Artwork_300DPI.png")

create_p6_wave_artwork()

# P7 Hex-Matrix
def create_p7_hex_artwork():
    W, H = 2800, 2200
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    hex_r = 75
    w_step = int(hex_r * math.sqrt(3))
    h_step = int(hex_r * 1.5)
    
    def draw_single_hex(cx, cy, r, fill, outline):
        pts = []
        for a in range(6):
            rad = math.radians(60 * a - 30)
            pts.append((cx + r * math.cos(rad), cy + r * math.sin(rad)))
        draw.polygon(pts, fill=fill, outline=outline)

    for row, cy in enumerate(range(300, H + 100, h_step)):
        x_shift = (w_step // 2) if row % 2 == 1 else 0
        for cx in range(100 + x_shift, W + 100, w_step):
            dist_flank = min(cx, W - cx) / (W / 2)
            if dist_flank < 0.65 or cy > H - 800:
                intensity = 1.0 - dist_flank
                alpha = int(240 * intensity)
                gold_hex = (row + cx // 100) % 7 == 0
                fill_c = (255, 184, 0, alpha) if gold_hex else (30, 58, 138, int(alpha * 0.7))
                out_c = (255, 230, 102, alpha) if gold_hex else (6, 182, 212, alpha)
                draw_single_hex(cx, cy, int(hex_r * 0.88), fill_c, out_c)

    img.save(os.path.join(output_dir, "P7_Hex_Matrix_Front_Artwork_300DPI.png"), dpi=(300, 300))
    print("Saved P7_Hex_Matrix_Front_Artwork_300DPI.png")

create_p7_hex_artwork()

# P8 Speed-Block
def create_p8_block_artwork():
    W, H = 2800, 2200
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    bands = [
        {"y_start": H - 150, "height": 130, "color": (255, 184, 0, 255), "angle": -16},
        {"y_start": H - 320, "height": 160, "color": (230, 57, 70, 255), "angle": -16},
        {"y_start": H - 520, "height": 180, "color": (30, 58, 138, 255), "angle": -16},
        {"y_start": H - 740, "height": 90,  "color": (255, 184, 0, 255), "angle": -16},
        {"y_start": H - 860, "height": 70,  "color": (255, 255, 255, 220), "angle": -16},
        {"y_start": H - 960, "height": 45,  "color": (6, 182, 212, 255), "angle": -16}
    ]
    
    for b in bands:
        h = b["height"]
        rad = math.radians(b["angle"])
        tan_a = math.tan(rad)
        pts = [
            (0, int(b["y_start"])),
            (W, int(b["y_start"] + W * tan_a)),
            (W, int(b["y_start"] + W * tan_a + h)),
            (0, int(b["y_start"] + h))
        ]
        draw.polygon(pts, fill=b["color"])

    img.save(os.path.join(output_dir, "P8_Speed_Block_Front_Artwork_300DPI.png"), dpi=(300, 300))
    print("Saved P8_Speed_Block_Front_Artwork_300DPI.png")

create_p8_block_artwork()

# P9 Cyber-Stream
def create_p9_stream_artwork():
    W, H = 2800, 2200
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    for i in range(16):
        pts = []
        y_base = H - 200 - i * 110
        for x in range(0, W + 60, 40):
            y = int(y_base + math.sin(x / 300.0) * 120 - (x / W) * 450)
            pts.append((x, y))
        col = (255, 184, 0, 240) if i % 3 == 0 else (6, 182, 212, 220)
        draw.line(pts, fill=col, width=32 - i, joint="curve")
        
    img.save(os.path.join(output_dir, "P9_Cyber_Stream_Front_Artwork_300DPI.png"), dpi=(300, 300))
    print("Saved P9_Cyber_Stream_Front_Artwork_300DPI.png")

create_p9_stream_artwork()

# P10 Prism-Grid
def create_p10_prism_artwork():
    W, H = 2800, 2200
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    step_x = 220
    step_y = 160
    
    for row, y in enumerate(range(H - 1200, H + 200, step_y)):
        for col, x in enumerate(range(-100, W + 200, step_x)):
            x_mid = x + (step_x // 2 if row % 2 == 1 else 0)
            tri_pts = [(x_mid, y), (x_mid + step_x // 2, y + step_y), (x_mid - step_x // 2, y + step_y)]
            alpha = int(220 * ((y - (H - 1200)) / 1400.0))
            is_gold = (row * 3 + col) % 5 == 0
            f_col = (255, 184, 0, alpha) if is_gold else (50, 60, 80, int(alpha * 0.6))
            out_col = (255, 230, 102, alpha) if is_gold else (100, 120, 150, alpha)
            draw.polygon(tri_pts, fill=f_col, outline=out_col)

    img.save(os.path.join(output_dir, "P10_Prism_Grid_Front_Artwork_300DPI.png"), dpi=(300, 300))
    print("Saved P10_Prism_Grid_Front_Artwork_300DPI.png")

create_p10_prism_artwork()

# 3. Full 4-Quadrant Vendor Specification Pack Sheets
def build_bundle_sheet(option_code, style_title, fabric_type, front_art_file, back_print_file, back_label, filename, is_collar=False):
    W, H = 3500, 2400
    sheet = Image.new("RGBA", (W, H), (10, 25, 47, 255))
    draw = ImageDraw.Draw(sheet)
    
    font_title = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 95)
    font_h2 = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 60)
    font_body = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 42)
    font_small = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 34)
    font_mono = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 36)
    
    # Header Banner
    draw.rectangle([(0, 0), (W, 200)], fill=(17, 34, 64, 255))
    draw.line([(0, 200), (W, 200)], fill=(255, 184, 0, 255), width=6)
    
    draw.text((60, 35), "UJJAIN DISTRICT TABLE TENNIS ASSOCIATION (UDTTA)", font=font_title, fill=(255, 184, 0, 255))
    tagline = f"PRODUCTION SPECIFICATION & PRINT-READY ASSETS PACK • {option_code}: {style_title.upper()}"
    draw.text((60, 135), tagline, font=font_h2, fill=(255, 255, 255, 255))
    
    # 4 Quadrants
    # Q1: Left Chest Crest (Top Left)
    draw.rectangle([(60, 240), (1680, 1240)], fill=(7, 13, 24, 255), outline=(255, 184, 0, 100), width=3)
    draw.rectangle([(60, 240), (1680, 320)], fill=(30, 58, 138, 200))
    draw.text((80, 255), "1. LEFT CHEST CREST & RIGHT SLEEVE EMBLEMS", font=font_h2, fill=(255, 255, 255, 255))
    
    # Paste Chest Logo
    chest_thumb = logo.resize((480, 480), Image.Resampling.LANCZOS)
    sheet.alpha_composite(chest_thumb, (120, 380))
    
    sleeve_thumb = logo.resize((380, 380), Image.Resampling.LANCZOS)
    sheet.alpha_composite(sleeve_thumb, (680, 430))
    
    draw.text((1150, 380), "• Left Chest Size: 3.5\" × 3.5\" (1050×1050 px)", font=font_body, fill=(255, 255, 255, 255))
    draw.text((1150, 460), "• Right Sleeve Size: 3.0\" × 3.0\" (900×900 px)", font=font_body, fill=(255, 255, 255, 255))
    draw.text((1150, 540), "• Process: Direct Dye Sublimation / DTF Transfer", font=font_body, fill=(255, 184, 0, 255))
    draw.text((1150, 620), f"• Base Fabric: {fabric_type}", font=font_body, fill=(255, 255, 255, 255))
    draw.text((1150, 700), "• Resolution: 300 DPI Transparent Alpha Channel", font=font_body, fill=(255, 255, 255, 255))
    draw.text((1150, 780), "• Position: 7.5\" from shoulder seam (Left Chest)", font=font_body, fill=(148, 163, 184, 255))
    draw.text((1150, 860), "• Sleeve: Centered on Right Bicep panel", font=font_body, fill=(148, 163, 184, 255))
    
    # Q2: Back Name & Number Typography (Top Right)
    draw.rectangle([(1760, 240), (3440, 1240)], fill=(7, 13, 24, 255), outline=(255, 184, 0, 100), width=3)
    draw.rectangle([(1760, 240), (3440, 320)], fill=(30, 58, 138, 200))
    draw.text((1780, 255), f"2. BACK TYPOGRAPHY & NUMBER SYSTEM ({back_label})", font=font_h2, fill=(255, 255, 255, 255))
    
    # Paste Back Print
    if os.path.exists(back_print_file):
        back_img = Image.open(back_print_file).convert("RGBA")
        back_thumb = back_img.resize((700, 816), Image.Resampling.LANCZOS)
        sheet.alpha_composite(back_thumb, (1800, 360))
        
    draw.text((2560, 380), "• Total Print Area: 12\" W × 16\" H", font=font_body, fill=(255, 255, 255, 255))
    draw.text((2560, 460), "• 'UJJAIN' Arch: 2.2\" H × 10\" W (Impact)", font=font_body, fill=(255, 255, 255, 255))
    draw.text((2560, 540), f"• Player Name: {back_label.split()[0]} (1.8\" H)", font=font_body, fill=(255, 184, 0, 255))
    draw.text((2560, 620), "• Number Height: 7.5\" H (Sports Block Outline)", font=font_body, fill=(255, 255, 255, 255))
    draw.text((2560, 700), "• Fill Color: Pure White (#FFFFFF)", font=font_body, fill=(255, 255, 255, 255))
    draw.text((2560, 780), "• Stroke Outline: Ujjain Gold 3mm (#FFB800)", font=font_body, fill=(255, 184, 0, 255))
    draw.text((2560, 860), "• Offset from collar: 3.5\" below neck ribbing", font=font_body, fill=(148, 163, 184, 255))
    
    # Q3: Front Torso Sublimation Graphics (Bottom Left)
    draw.rectangle([(60, 1300), (1680, 2320)], fill=(7, 13, 24, 255), outline=(255, 184, 0, 100), width=3)
    draw.rectangle([(60, 1300), (1680, 1380)], fill=(30, 58, 138, 200))
    draw.text((80, 1315), "3. FRONT TORSO SUBLIMATION / PRINT ARTWORK", font=font_h2, fill=(255, 255, 255, 255))
    
    if os.path.exists(front_art_file):
        art_img = Image.open(front_art_file).convert("RGBA")
        art_thumb = art_img.resize((1000, 785), Image.Resampling.LANCZOS)
        sheet.alpha_composite(art_thumb, (120, 1430))
        
    draw.text((1150, 1440), "• Art Dimensions: 14\" W × 18\" H", font=font_body, fill=(255, 255, 255, 255))
    draw.text((1150, 1520), "• Sublimation Heat: 200°C @ 45s", font=font_body, fill=(255, 184, 0, 255))
    draw.text((1150, 1600), "• Seamless Bleed: 0.5\" across side hems", font=font_body, fill=(255, 255, 255, 255))
    draw.text((1150, 1680), "• Ink Type: Fluorescent / Vibrant Sports Ink", font=font_body, fill=(255, 255, 255, 255))
    draw.text((1150, 1760), "• Color Profile: CMYK U.S. Web Coated", font=font_body, fill=(148, 163, 184, 255))
    
    # Q4: Color Codes & Factory Checklist (Bottom Right)
    draw.rectangle([(1760, 1300), (3440, 2320)], fill=(7, 13, 24, 255), outline=(255, 184, 0, 100), width=3)
    draw.rectangle([(1760, 1300), (3440, 1380)], fill=(30, 58, 138, 200))
    draw.text((1780, 1315), "4. FACTORY COLOR PALETTE & QC TOLERANCES", font=font_h2, fill=(255, 255, 255, 255))
    
    # Swatches
    swatches = [
        {"name": "Deep Navy Blue", "hex": "#0A192F", "pms": "PMS 289 C", "rgb": (10, 25, 47)},
        {"name": "Ujjain Gold", "hex": "#FFB800", "pms": "PMS 123 C", "rgb": (255, 184, 0)},
        {"name": "Crimson Red", "hex": "#E63946", "pms": "PMS 1795 C", "rgb": (230, 57, 70)},
        {"name": "Aero Cyan", "hex": "#06B6D4", "pms": "PMS 3115 C", "rgb": (6, 182, 212)},
        {"name": "Midnight Carbon", "hex": "#111115", "pms": "PMS Black C", "rgb": (17, 17, 21)}
    ]
    
    for i, s in enumerate(swatches):
        sy = 1430 + i * 110
        draw.rectangle([(1800, sy), (1960, sy + 85)], fill=s["rgb"], outline=(255, 255, 255, 180), width=2)
        draw.text((2000, sy + 5), f"{s['name']}", font=font_body, fill=(255, 255, 255, 255))
        draw.text((2000, sy + 48), f"{s['hex']}  |  {s['pms']}", font=font_mono, fill=(255, 184, 0, 255))
        
    draw.text((2650, 1440), "QUALITY CONTROL GATES:", font=font_h2, fill=(255, 184, 0, 255))
    draw.text((2650, 1530), "✔ Crest placement ±2mm horizontal tolerance", font=font_small, fill=(255, 255, 255, 255))
    draw.text((2650, 1600), "✔ Sublimation color vibrancy fastness level 4+", font=font_small, fill=(255, 255, 255, 255))
    draw.text((2650, 1670), "✔ Anti-pilling & moisture-wicking tested", font=font_small, fill=(255, 255, 255, 255))
    draw.text((2650, 1740), "✔ Collar ribbed tipping aligned to placket", font=font_small, fill=(255, 255, 255, 255))
    draw.text((2650, 1810), "✔ Back numbers centered to garment centerline", font=font_small, fill=(255, 255, 255, 255))
    
    sheet.save(os.path.join(output_dir, filename), dpi=(300, 300))
    print(f"Saved {filename}")

# Generate Full Print Spec Packs for all P1 through P10
build_bundle_sheet("P1", "Solar Flare Navy Flame V-Neck", "100% Micro-Mesh Polyester (160 GSM)", 
                   os.path.join(output_dir, "P1_Solar_Flare_Front_Artwork_300DPI.png"), 
                   os.path.join(output_dir, "P1_Back_Print_SHARMA_07_300DPI.png"), 
                   "SHARMA #07", "P1_Full_Print_Bundle_300DPI.png")

build_bundle_sheet("P2", "Carbon Black Flame V-Neck", "100% Micro-Mesh Polyester (160 GSM)", 
                   os.path.join(output_dir, "P2_Carbon_Flame_Front_Artwork_300DPI.png"), 
                   os.path.join(output_dir, "P2_Back_Print_SHARMA_07_300DPI.png"), 
                   "SHARMA #07", "P2_Full_Print_Bundle_300DPI.png")

build_bundle_sheet("P3", "Crimson Speed Raglan V-Neck", "100% Micro-Mesh Polyester (160 GSM)", 
                   os.path.join(output_dir, "P3_Speed_Raglan_Front_Artwork_300DPI.png"), 
                   os.path.join(output_dir, "P3_Back_Print_VERMA_10_300DPI.png"), 
                   "VERMA #10", "P3_Full_Print_Bundle_300DPI.png")

build_bundle_sheet("P4", "Solar Flare Collared Polo (Navy)", "100% Performance Polyester Polo (160 GSM)", 
                   os.path.join(output_dir, "P4_Solar_Flare_Front_Artwork_300DPI.png"), 
                   os.path.join(output_dir, "P4_Back_Print_AARAV_07_300DPI.png"), 
                   "AARAV #07", "P4_Full_Print_Bundle_300DPI.png", is_collar=True)

build_bundle_sheet("P5", "Carbon Flame Collared Polo (Black)", "100% Performance Polyester Polo (160 GSM)", 
                   os.path.join(output_dir, "P5_Carbon_Flame_Front_Artwork_300DPI.png"), 
                   os.path.join(output_dir, "P5_Back_Print_SHARMA_07_300DPI.png"), 
                   "SHARMA #07", "P5_Full_Print_Bundle_300DPI.png", is_collar=True)

build_bundle_sheet("P6", "Donic Aero-Wave Collared Polo (Navy)", "100% Performance Polyester Polo (160 GSM)", 
                   os.path.join(output_dir, "P6_Aero_Wave_Front_Artwork_300DPI.png"), 
                   os.path.join(output_dir, "P6_Back_Print_SINGH_11_300DPI.png"), 
                   "SINGH #11", "P6_Full_Print_Bundle_300DPI.png", is_collar=True)

build_bundle_sheet("P7", "Butterfly Hex-Matrix Polo (Black)", "100% Performance Polyester Polo (160 GSM)", 
                   os.path.join(output_dir, "P7_Hex_Matrix_Front_Artwork_300DPI.png"), 
                   os.path.join(output_dir, "P7_Back_Print_MEHTA_14_300DPI.png"), 
                   "MEHTA #14", "P7_Full_Print_Bundle_300DPI.png", is_collar=True)

build_bundle_sheet("P8", "Tibhar Speed-Block Polo (Navy)", "100% Performance Polyester Polo (160 GSM)", 
                   os.path.join(output_dir, "P8_Speed_Block_Front_Artwork_300DPI.png"), 
                   os.path.join(output_dir, "P8_Back_Print_GUPTA_18_300DPI.png"), 
                   "GUPTA #18", "P8_Full_Print_Bundle_300DPI.png", is_collar=True)

build_bundle_sheet("P9", "Xiom Cyber-Stream Kinetic V-Neck", "100% Micro-Mesh Polyester (160 GSM)", 
                   os.path.join(output_dir, "P9_Cyber_Stream_Front_Artwork_300DPI.png"), 
                   os.path.join(output_dir, "P9_Back_Print_JOSHI_21_300DPI.png"), 
                   "JOSHI #21", "P9_Full_Print_Bundle_300DPI.png")

build_bundle_sheet("P10", "Stiga Prism-Grid Facet V-Neck", "100% Micro-Mesh Polyester (160 GSM)", 
                   os.path.join(output_dir, "P10_Prism_Grid_Front_Artwork_300DPI.png"), 
                   os.path.join(output_dir, "P10_Back_Print_PATEL_23_300DPI.png"), 
                   "PATEL #23", "P10_Full_Print_Bundle_300DPI.png")

# 4. Master Specification Pack for Officials & Referees (100% Clean Blank Back)
def build_official_spec_sheet():
    W, H = 3500, 2400
    sheet = Image.new("RGBA", (W, H), (10, 25, 47, 255))
    draw = ImageDraw.Draw(sheet)
    
    font_title = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 95)
    font_h2 = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 60)
    font_body = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 42)
    font_small = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 34)
    font_mono = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 36)
    
    # Header Banner
    draw.rectangle([(0, 0), (W, 200)], fill=(15, 23, 42, 255))
    draw.line([(0, 200), (W, 200)], fill=(255, 184, 0, 255), width=6)
    
    draw.text((60, 35), "UJJAIN DISTRICT TABLE TENNIS ASSOCIATION (UDTTA)", font=font_title, fill=(255, 184, 0, 255))
    tagline = "OFFICIALS & REFEREES 100% COTTON POLO EMBROIDERY & PRODUCTION MASTER PACK (O1 - O10)"
    draw.text((60, 135), tagline, font=font_h2, fill=(255, 255, 255, 255))
    
    # Q1: Left Chest Embroidery Badge
    draw.rectangle([(60, 240), (1680, 1240)], fill=(7, 13, 24, 255), outline=(255, 184, 0, 100), width=3)
    draw.rectangle([(60, 240), (1680, 320)], fill=(30, 41, 59, 200))
    draw.text((80, 255), "1. LEFT CHEST HIGH-DENSITY EMBROIDERY SPEC", font=font_h2, fill=(255, 184, 0, 255))
    
    chest_thumb = logo.resize((500, 500), Image.Resampling.LANCZOS)
    sheet.alpha_composite(chest_thumb, (120, 370))
    
    draw.text((700, 380), "• Dimensions: 3.5\" × 3.5\" (88.9 mm diameter)", font=font_body, fill=(255, 255, 255, 255))
    draw.text((700, 460), "• Stitch Count: ~14,500 High-Density Stitches", font=font_body, fill=(255, 184, 0, 255))
    draw.text((700, 540), "• Thread Type: Madeira Polyneon 40 / Rayon", font=font_body, fill=(255, 255, 255, 255))
    draw.text((700, 620), "• Placement: 7.5\" below shoulder seam, center left", font=font_body, fill=(255, 255, 255, 255))
    draw.text((700, 700), "• Backing: Cutaway non-woven stabilizer 2.5 oz", font=font_body, fill=(148, 163, 184, 255))
    
    # Q2: Right Sleeve Badge Spec
    draw.rectangle([(1760, 240), (3440, 1240)], fill=(7, 13, 24, 255), outline=(255, 184, 0, 100), width=3)
    draw.rectangle([(1760, 240), (3440, 320)], fill=(30, 41, 59, 200))
    draw.text((1780, 255), "2. RIGHT SLEEVE EMBROIDERY / TRANSFER SPEC", font=font_h2, fill=(255, 184, 0, 255))
    
    sleeve_thumb = logo.resize((480, 480), Image.Resampling.LANCZOS)
    sheet.alpha_composite(sleeve_thumb, (1820, 380))
    
    draw.text((2360, 380), "• Dimensions: 3.0\" × 3.0\" (76.2 mm diameter)", font=font_body, fill=(255, 255, 255, 255))
    draw.text((2360, 460), "• Stitch Count: ~10,200 High-Density Stitches", font=font_body, fill=(255, 184, 0, 255))
    draw.text((2360, 540), "• Placement: Centered on Right Sleeve bicep", font=font_body, fill=(255, 255, 255, 255))
    draw.text((2360, 620), "• Offset: 1.5\" above bottom sleeve cuff hem", font=font_body, fill=(255, 255, 255, 255))
    draw.text((2360, 700), "• Process: Precision Direct Embroidery or DTF", font=font_body, fill=(148, 163, 184, 255))
    
    # Q3: 100% Clean Blank Back Rule
    draw.rectangle([(60, 1300), (1680, 2320)], fill=(7, 13, 24, 255), outline=(16, 185, 129, 150), width=3)
    draw.rectangle([(60, 1300), (1680, 1380)], fill=(6, 78, 59, 200))
    draw.text((80, 1315), "3. MANDATORY 100% CLEAN SOLID BLANK BACK", font=font_h2, fill=(52, 211, 153, 255))
    
    draw.text((100, 1430), "STRICT OFFICIAL PROTOCOL REQUIREMENT:", font=font_h2, fill=(255, 184, 0, 255))
    draw.text((100, 1520), "• Zero text, zero player names, and zero numbers on back.", font=font_body, fill=(255, 255, 255, 255))
    draw.text((100, 1600), "• Solid pristine pique cotton dyed fabric only.", font=font_body, fill=(255, 255, 255, 255))
    draw.text((100, 1680), "• Structured polo collar with gold / accent tipping.", font=font_body, fill=(255, 255, 255, 255))
    draw.text((100, 1760), "• Reinforced 2-button placket with tone-on-tone buttons.", font=font_body, fill=(255, 255, 255, 255))
    draw.text((100, 1840), "• Fabric: 100% Heavyweight Combed Cotton Pique (220 GSM).", font=font_body, fill=(52, 211, 153, 255))
    
    # Q4: Official Options List O1 - O10
    draw.rectangle([(1760, 1300), (3440, 2320)], fill=(7, 13, 24, 255), outline=(255, 184, 0, 100), width=3)
    draw.rectangle([(1760, 1300), (3440, 1380)], fill=(30, 41, 59, 200))
    draw.text((1780, 1315), "4. OFFICIAL OPTIONS (O1 TO O10) PRODUCTION MATRIX", font=font_h2, fill=(255, 255, 255, 255))
    
    off_list = [
        "O1: Executive Navy Polo (Gold Tipping)",
        "O2: Stealth Midnight Black Polo (Gold Tipping)",
        "O3: Royal Blue & Navy Contrast Polo",
        "O4: Executive Slate Charcoal Polo",
        "O5: Ceremonial Burgundy / Crimson Polo",
        "O6: Dual-Tipped Navy & Crimson Polo",
        "O7: Tactical Monochrome Black Polo",
        "O8: Dark Steel Blue Pique Polo",
        "O9: Deep Forest Pine Polo",
        "O10: Carbon Slate & Navy Contrast Polo"
    ]
    for i, o_text in enumerate(off_list):
        oy = 1420 + i * 85
        col = (255, 184, 0, 255) if i == 0 else (255, 255, 255, 255)
        draw.text((1800, oy), f"✔ {o_text}", font=font_body, fill=col)

    sheet.save(os.path.join(output_dir, "Official_Master_Spec_Pack_300DPI.png"), dpi=(300, 300))
    print("Saved Official_Master_Spec_Pack_300DPI.png")

build_official_spec_sheet()

print("ALL GRAPHICS ASSETS SUCCESSFULLY GENERATED!")
