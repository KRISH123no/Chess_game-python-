import pygame

class Menu:
    def __init__(self, screen, settings, ui):
        self.screen = screen
        self.settings = settings
        self.ui = ui
        
        self.font_title = settings.get_font(84)
        self.font_btn = settings.get_font(28)
        self.font_small = settings.get_font(20)

        # Base Button Rects (Centers updated in draw)
        self.btn_w, self.btn_h = 350, 60
        self.ai_btn = pygame.Rect(0, 320, self.btn_w, self.btn_h)
        self.friend_btn = pygame.Rect(0, 410, self.btn_w, self.btn_h)
        self.settings_btn = pygame.Rect(0, 500, self.btn_w, self.btn_h)
        self.back_btn = pygame.Rect(30, 30, 120, 45)

        self.diff_buttons = {
            "Easy": pygame.Rect(0, 250, self.btn_w, 55),
            "Medium": pygame.Rect(0, 320, self.btn_w, 55),
            "Hard": pygame.Rect(0, 390, self.btn_w, 55),
            "Pro": pygame.Rect(0, 460, self.btn_w, 55)
        }

    def draw_wood_bg(self):
        w, h = self.screen.get_size()
        self.screen.fill(self.settings.WOOD_BASE)
        # Dynamic grain lines across full width
        for i in range(0, h, 4):
            color = self.settings.WOOD_GRAIN_MID if (i // 4) % 2 == 0 else self.settings.WOOD_BASE
            pygame.draw.line(self.screen, color, (0, i), (w, i), 2)

    def draw_premium_button(self, rect, text, is_hovered):
        # Draw dynamic button with tavern style
        body_color = (90, 45, 20) if is_hovered else self.settings.WOOD_GRAIN_MID
        pygame.draw.rect(self.screen, body_color, rect, border_radius=10)
        pygame.draw.rect(self.screen, self.settings.ACCENT_COLOR, rect, width=3, border_radius=10)
        
        txt_surf = self.font_btn.render(text, True, self.settings.TEXT_COLOR)
        txt_rect = txt_surf.get_rect(center=rect.center)
        self.screen.blit(txt_surf, txt_rect)

    def draw_main_menu(self):
        w, h = self.screen.get_size()
        cx = w // 2
        
        # Reposition based on current size
        self.ai_btn.centerx = cx
        self.friend_btn.centerx = cx
        self.settings_btn.centerx = cx

        title = self.font_title.render("Chess", True, self.settings.ACCENT_COLOR)
        self.screen.blit(title, (cx - title.get_width()//2, 100))
        
        m_pos = pygame.mouse.get_pos()
        self.draw_premium_button(self.ai_btn, "Player vs AI", self.ai_btn.collidepoint(m_pos))
        self.draw_premium_button(self.friend_btn, "vs Friend", self.friend_btn.collidepoint(m_pos))
        self.draw_premium_button(self.settings_btn, "Settings", self.settings_btn.collidepoint(m_pos))

    def draw_difficulty_menu(self):
        w, h = self.screen.get_size()
        cx = w // 2
        
        self.draw_premium_button(self.back_btn, "Back", self.back_btn.collidepoint(pygame.mouse.get_pos()))
        
        m_pos = pygame.mouse.get_pos()
        for label, rect in self.diff_buttons.items():
            rect.centerx = cx
            self.draw_premium_button(rect, label, rect.collidepoint(m_pos))

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.ai_btn.collidepoint(event.pos): return 'VS_AI'
                if self.friend_btn.collidepoint(event.pos): return 'VS_FRIEND'
                if self.settings_btn.collidepoint(event.pos): return 'SETTINGS'
        return None

    def update_difficulty(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_btn.collidepoint(event.pos): return 'BACK'
                for label, rect in self.diff_buttons.items():
                    if rect.collidepoint(event.pos): return label.upper()
        return None