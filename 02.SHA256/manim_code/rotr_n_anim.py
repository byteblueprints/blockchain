from manim import *

class Rotr32Anim(Scene):
    def construct(self):
        font = "Consolas"
        bit_font_size = 20
        box_size = 0.32
        bit_count = 32
        rotate_total = 5  # Number of rotations to show

        # Title
        rotr_title = Text("ROTR5 (Rotate Right by 5)", font_size=40, font=font)
        self.play(Write(rotr_title))
        self.play(rotr_title.animate.to_edge(UP))
        self.wait(0.5)

        # Initial bits (alternating pattern for clarity)
        bits = ["1" if i % 2 == 0 else "0" for i in range(bit_count)]
        boxes = VGroup(*[Square(box_size) for _ in range(bit_count)])
        boxes.arrange(RIGHT, buff=0.01)
        boxes.next_to(rotr_title, DOWN, buff=0.7)
        boxes.scale(0.95)
        self.play(FadeIn(boxes))

        bit_mobs = VGroup(*[Text(bit, font_size=bit_font_size, font=font).move_to(boxes[i]) for i, bit in enumerate(bits)])
        self.play(FadeIn(bit_mobs))
        self.wait(0.7)

        # Rotate right animation
        for rotate_num in range(1, rotate_total + 1):
            animations = []
            # Animate all bits moving right
            for i in range(bit_count-1, 0, -1):
                animations.append(bit_mobs[i-1].animate.move_to(boxes[i]))
            # Animate the last bit wrapping around to the first box
            wrap_bit = bit_mobs[-1]
            animations.append(wrap_bit.animate.move_to(boxes[0]))
            self.play(*animations, run_time=0.7)
            self.wait(0.3)
            # Reorder bit_mobs to reflect the new order after rotation
            bit_mobs = VGroup(wrap_bit, *bit_mobs[:-1])

        self.wait(1)
        self.play(FadeOut(bit_mobs), FadeOut(boxes), FadeOut(rotr_title))
        self.wait(0.5) 