from manim import *
import numpy as np

class SVDAnimation(Scene):
    def construct(self):
        # Mathematical Setup
        # We use the shear matrix as an example
        A = np.array([[1, 1], 
                      [0, 1]])
        U, S, Vt = np.linalg.svd(A)
        Sigma = np.diag(S)

        # Create the Grid and Circle
        # Create a grid manually so we can control it
        grid = NumberPlane(
            x_range=[-25, 25, 1],
            y_range=[-25, 25, 1],
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )
        circle = Circle(radius=1, color=YELLOW, stroke_width=4)
        
        # Group them together so we can transform them as one unit
        # This represents "Vector Space"
        vector_space = VGroup(grid, circle)
        
        self.add(vector_space)

        # Create the Static Label
        label = MathTex(r"\text{Original Space}").to_edge(UP)
        label.add_background_rectangle(opacity=0.8)
        
        self.play(Write(label))
        self.wait(1)

        # Rotation (V transpose)
        # Update text
        label_step1 = MathTex(r"\text{Step 1: Rotate } (V^T)").to_edge(UP)
        label_step1.add_background_rectangle(opacity=0.8)
        
        self.play(
            ReplacementTransform(label, label_step1),
            # ApplyMatrix only to the vector_space, ignoring the text
            ApplyMatrix(Vt, vector_space),
            run_time=2
        )
        self.wait(1)

        # Stretch (Sigma)
        label_step2 = MathTex(r"\text{Step 2: Stretch } (\Sigma)").to_edge(UP)
        label_step2.add_background_rectangle(opacity=0.8)

        self.play(
            ReplacementTransform(label_step1, label_step2),
            ApplyMatrix(Sigma, vector_space),
            run_time=2
        )
        self.wait(1)

        # Rotation (U)
        label_step3 = MathTex(r"\text{Step 3: Rotate } (U)").to_edge(UP)
        label_step3.add_background_rectangle(opacity=0.8)

        self.play(
            ReplacementTransform(label_step2, label_step3),
            ApplyMatrix(U, vector_space),
            run_time=2
        )
        self.wait(1)

        a_text = MathTex("A = ")
        
        # Create the Matrix visual
        # num_decimal_places=0 will show integers instead of floats
        matrix_visual = DecimalMatrix(A, num_decimal_places=0, include_background_rectangle=False)
        matrix_visual.set_color(WHITE)

        # Group them together side-by-side
        final_group = VGroup(a_text, matrix_visual).arrange(RIGHT)
        final_group.to_edge(UP)
        
        # Add background to the whole group so grid lines don't show through the numbers
        final_group.add_background_rectangle(opacity=0.8)
        self.play(ReplacementTransform(label_step3, final_group))
        self.wait(1)