from manim import *

class AddNAnim(Scene):
    def construct(self):
        font = "Consolas"
        bit_font_size = 20
        box_size = 0.32
        bit_count = 16  # For clarity in animation

        # Example values
        x_bits = ["1" if i % 2 == 0 else "0" for i in range(bit_count)]
        y_bits = ["0" if i % 3 == 0 else "1" for i in range(bit_count)]
        x_val = int("".join(x_bits), 2)
        y_val = int("".join(y_bits), 2)
        sum_val = (x_val + y_val) % (1 << bit_count)
        sum_bits = list(format(sum_val, f'0{bit_count}b'))

        # Compute carry bits for visualization
        carry = [0] * (bit_count + 1)
        for i in range(bit_count-1, -1, -1):
            xi = int(x_bits[i])
            yi = int(y_bits[i])
            carry[i] = (xi + yi + carry[i+1]) // 2
        carry_bits = [str(c) for c in carry[1:]]

        # Title
        add_title = Text("Binary Addition", font_size=40, font=font)
        self.play(Write(add_title))
        self.play(add_title.animate.to_edge(UP))
        self.wait(0.5)

        # Bit rows
        def make_row(bits, y_offset, label):
            boxes = VGroup(*[Square(box_size) for _ in range(bit_count)])
            boxes.arrange(RIGHT, buff=0.01)
            boxes.shift(UP * y_offset)
            bit_mobs = VGroup(*[Text(bit, font_size=bit_font_size, font=font).move_to(boxes[i]) for i, bit in enumerate(bits)])
            label_mob = Text(label, font_size=24, font=font).next_to(boxes, LEFT, buff=0.3)
            return boxes, bit_mobs, label_mob

        carry_boxes, carry_mobs, carry_label = make_row(carry_bits, 1.5, "Carry")
        x_boxes, x_mobs, x_label = make_row(x_bits, 0.5, "X")
        y_boxes, y_mobs, y_label = make_row(y_bits, -0.5, "Y")
        sum_boxes, sum_mobs, sum_label = make_row(["?" for _ in range(bit_count)], -1.5, "Sum")

        self.play(FadeIn(carry_boxes), FadeIn(carry_mobs), FadeIn(carry_label))
        self.play(FadeIn(x_boxes), FadeIn(x_mobs), FadeIn(x_label))
        self.play(FadeIn(y_boxes), FadeIn(y_mobs), FadeIn(y_label))
        self.play(FadeIn(sum_boxes), FadeIn(sum_label))
        self.wait(0.5)

        # Animate sum result
        for i in range(bit_count):
            self.play(Transform(sum_mobs[i], Text(sum_bits[i], font_size=bit_font_size, font=font).move_to(sum_boxes[i])), run_time=0.2)
        self.wait(1)
        self.play(FadeOut(carry_boxes), FadeOut(carry_mobs), FadeOut(carry_label),
                  FadeOut(x_boxes), FadeOut(x_mobs), FadeOut(x_label),
                  FadeOut(y_boxes), FadeOut(y_mobs), FadeOut(y_label),
                  FadeOut(sum_boxes), FadeOut(sum_mobs), FadeOut(sum_label),
                  FadeOut(add_title))
        self.wait(0.5) 