from manim import *

class SHA256Intro(Scene):
    def construct(self):
        # --- Config ---
        font = "Calibri"
        bit_font_size = 36
        box_size = 0.7
        bit_count = 8
        shift_total = 3

        # --- Title ---
        shr_title = Text("SHR3", font_size=48, font=font)
        self.play(Write(shr_title))
        self.play(shr_title.animate.to_edge(UP))
        self.wait(0.5)

        # --- Helper to create bit VGroup ---
        def make_bits(bits, boxes):
            return VGroup(*[
                Text(bit, font_size=bit_font_size, font=font).move_to(box)
                for bit, box in zip(bits, boxes)
            ])

        # --- Boxes and bits ---
        bits = ["1", "0", "1", "1", "0", "1", "0", "1"]
        boxes = VGroup(*[Square(box_size) for _ in range(bit_count)])
        boxes.arrange(RIGHT, buff=0.08).next_to(shr_title, DOWN, buff=1)
        self.play(FadeIn(boxes))

        bit_mobs = make_bits(bits, boxes)
        self.play(FadeIn(bit_mobs))
        self.wait(0.7)

        # --- Shift counter ---
        shift_counter = Text("Shift: 0", font_size=32, font=font)
        shift_counter.next_to(boxes, DOWN, buff=0.5)
        self.play(FadeIn(shift_counter))

        # --- Shift animation ---
        for shift_num in range(1, shift_total + 1):
            # Animate all bits moving right (except the last one)
            animations = [
                bit_mobs[i-1].animate.move_to(boxes[i])
                for i in range(bit_count-1, 0, -1)
            ]
            # Move the exiting bit out
            exiting_bit = bit_mobs[-1]
            exit_target = boxes[-1].get_center() + RIGHT * (box_size * 1.2)
            animations.append(exiting_bit.animate.move_to(exit_target))
            self.play(*animations, run_time=0.7)
            self.wait(0.3)

            # Fade out the exiting bit
            self.play(FadeOut(exiting_bit), run_time=0.4)
            self.wait(0.2)

            # Fade in new 0 in the start box
            new_zero = Text("0", font_size=bit_font_size, font=font).move_to(boxes[0])
            self.play(FadeIn(new_zero), run_time=0.4)
            self.wait(0.2)
            bit_mobs = VGroup(new_zero, *bit_mobs[:-1])

            # Update shift counter
            new_counter = Text(f"Shift: {shift_num}", font_size=32, font=font).move_to(shift_counter)
            self.play(Transform(shift_counter, new_counter), run_time=0.3)

        self.wait(1)
        self.play(FadeOut(bit_mobs), FadeOut(boxes), FadeOut(shift_counter))
        self.wait(0.5)

        # # --- 32-bit SHR animation (uncomment to use) ---
        # ... (your 32-bit code here, can be similarly optimized) ...

        # # --- 32-bit SHR animation ---
        # bits = ["1" if i % 2 == 0 else "0" for i in range(32)]
        # box_size = 0.32
        # boxes = VGroup(*[Square(box_size) for _ in range(32)])
        # boxes.arrange(RIGHT, buff=0.01)
        # boxes.next_to(shr32, DOWN, buff=0.7)
        # boxes.scale(0.95)
        # self.play(FadeIn(boxes))
        #
        # bit_mobs = VGroup(*[Text(bit, font_size=16, font="Consolas").move_to(boxes[i]) for i, bit in enumerate(bits)])
        # self.play(FadeIn(bit_mobs))
        # self.wait(0.7)
        #
        # for _ in range(32):
        #     animations = []
        #     for i in range(31, 0, -1):
        #         animations.append(bit_mobs[i-1].animate.move_to(boxes[i]))
        #     exiting_bit = bit_mobs[-1]
        #     exit_target = boxes[-1].get_center() + RIGHT * (box_size * 1.2)
        #     animations.append(exiting_bit.animate.move_to(exit_target))
        #     self.play(*animations, run_time=0.5)
        #     self.wait(0.2)
        #     self.play(FadeOut(exiting_bit), run_time=0.3)
        #     self.wait(0.2)
        #     new_zero = Text("0", font_size=16, font="Consolas").move_to(boxes[0])
        #     self.play(FadeIn(new_zero), run_time=0.3)
        #     self.wait(0.2)
        #     bit_mobs = VGroup(new_zero, *bit_mobs[:-1])
        #
        # self.wait(1)
        
        