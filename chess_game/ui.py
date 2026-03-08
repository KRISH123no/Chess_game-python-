import pygame

class UI:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.font_main = settings.get_font(32)
        self.font_status = settings.get_font(24)
        self.font_history = settings.get_font(18)
        
        # We define a fixed width for the panel, but its X position will be dynamic
        self.panel_width = 250
        self.go_back_btn = pygame.Rect(0, 0, 200, 50) # Positioned dynamically in draw

    def draw_side_panel(self, board, status_text, w, h):
        # 1. Calculate Dynamic Position
        # We want the panel to stay to the right of the board
        off_x, off_y = self.settings.get_offsets(w, h)
        panel_x = off_x + self.settings.BOARD_SIZE + 40
        panel_rect = pygame.Rect(panel_x, off_y, self.panel_width, self.settings.BOARD_SIZE)

        # 2. Draw Panel Background
        pygame.draw.rect(self.screen, self.settings.WOOD_GRAIN_MID, panel_rect, border_radius=10)
        pygame.draw.rect(self.screen, self.settings.ACCENT_COLOR, panel_rect, width=3, border_radius=10)
        
        # 3. Draw Status text
        status_color = (200, 0, 0) if "Check" in status_text else self.settings.TEXT_COLOR
        status_surf = self.font_status.render(status_text, True, status_color)
        self.screen.blit(status_surf, (panel_rect.x + 20, panel_rect.y + 20))

        # 4. Draw History Title
        history_surf = self.font_main.render("History", True, self.settings.ACCENT_COLOR)
        self.screen.blit(history_surf, (panel_rect.x + 20, panel_rect.y + 70))

    def draw_game_over(self, result):
        curr_w, curr_h = self.screen.get_size()
        
        # Dim the entire screen (Maximized or not)
        overlay = pygame.Surface((curr_w, curr_h), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.screen.blit(overlay, (0, 0))

        # Center the Message
        msg = "White Wins!" if result == "1-0" else "Black Wins!" if result == "0-1" else "Draw!"
        res_surf = self.font_main.render(msg, True, self.settings.ACCENT_COLOR)
        res_rect = res_surf.get_rect(center=(curr_w // 2, curr_h // 2 - 40))
        self.screen.blit(res_surf, res_rect)

        # Update Back Button Position and Draw
        self.go_back_btn.center = (curr_w // 2, curr_h // 2 + 50)
        pygame.draw.rect(self.screen, self.settings.WOOD_GRAIN_MID, self.go_back_btn, border_radius=10)
        pygame.draw.rect(self.screen, self.settings.ACCENT_COLOR, self.go_back_btn, width=2, border_radius=10)
        
        btn_txt = self.font_status.render("Main Menu", True, self.settings.TEXT_COLOR)
        self.screen.blit(btn_txt, btn_txt.get_rect(center=self.go_back_btn.center))