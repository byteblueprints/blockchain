from manim import *

class XorNAnim(Scene):
    def construct(self):
        font = "Consolas"
        bit_font_size = 20
        box_size = 0.32
        bit_count = 16  # For clarity in animation

        # Example values
        x_bits = ["1" if i % 2 == 0 else "0" for i in range(bit_count)]
        y_bits = ["0" if i % 3 == 0 else "1" for i in range(bit_count)]
        xor_bits = [str(int(a) ^ int(b)) for a, b in zip(x_bits, y_bits)]

        # Title
        xor_title = Text("XOR Operation", font_size=40, font=font)
        self.play(Write(xor_title))
        self.play(xor_title.animate.to_edge(UP))
        self.wait(0.5)

        # Bit rows
        def make_row(bits, y_offset, label):
            boxes = VGroup(*[Square(box_size) for _ in range(bit_count)])
            boxes.arrange(RIGHT, buff=0.01)
            boxes.shift(UP * y_offset)
            bit_mobs = VGroup(*[Text(bit, font_size=bit_font_size, font=font).move_to(boxes[i]) for i, bit in enumerate(bits)])
            label_mob = Text(label, font_size=24, font=font).next_to(boxes, LEFT, buff=0.3)
            return boxes, bit_mobs, label_mob

        x_boxes, x_mobs, x_label = make_row(x_bits, 1, "X")
        y_boxes, y_mobs, y_label = make_row(y_bits, 0, "Y")
        xor_boxes, xor_mobs, xor_label = make_row(["?" for _ in range(bit_count)], -1, "XOR")

        self.play(FadeIn(x_boxes), FadeIn(x_mobs), FadeIn(x_label))
        self.play(FadeIn(y_boxes), FadeIn(y_mobs), FadeIn(y_label))
        self.play(FadeIn(xor_boxes), FadeIn(xor_label))
        self.wait(0.5)

        # Animate XOR result
        for i in range(bit_count):
            self.play(Transform(xor_mobs[i], Text(xor_bits[i], font_size=bit_font_size, font=font).move_to(xor_boxes[i])), run_time=0.2)
        self.wait(1)
        self.play(FadeOut(x_boxes), FadeOut(x_mobs), FadeOut(x_label),
                  FadeOut(y_boxes), FadeOut(y_mobs), FadeOut(y_label),
                  FadeOut(xor_boxes), FadeOut(xor_mobs), FadeOut(xor_label),
                  FadeOut(xor_title))
        self.wait(0.5) 