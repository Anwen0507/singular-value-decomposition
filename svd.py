from manim import *
import numpy as np

class SVDAnimation(Scene):
    def construct(self):
        # Mathematical Setup
        A = np.array([[1, 1], 
                      [0, 1]])
        U, S, Vt = np.linalg.svd(A)
        Sigma = np.diag(S)

        # Create the Grid and Circle
        # Create a grid manually so we can control it
        grid = NumberPlane()
        circle = Circle(radius=1, color=YELLOW)
        
        # Group them together so we can transform them as one unit
        # This represents "Vector Space"
        vector_space = VGroup(grid, circle)
        
        self.add(vector_space)

        # Create the Static Label
        label = Text("Original Space", font_size=32).to_edge(UP)
        label.add_background_rectangle()
        
        self.play(Write(label))
        self.wait(1)

        # Rotation (V transpose)
        # Update text
        label_step1 = Text("Step 1: Rotate (V^T)", font_size=32).to_edge(UP)
        label_step1.add_background_rectangle()
        
        self.play(
            ReplacementTransform(label, label_step1),
            # ApplyMatrix only to the vector_space, ignoring the text
            ApplyMatrix(Vt, vector_space),
            run_time=2
        )
        self.wait(1)

        # Stretch (Sigma)
        label_step2 = Text("Step 2: Stretch (Sigma)", font_size=32).to_edge(UP)
        label_step2.add_background_rectangle()

        self.play(
            ReplacementTransform(label_step1, label_step2),
            ApplyMatrix(Sigma, vector_space),
            run_time=2
        )
        self.wait(1)

        # Rotation (U)
        label_step3 = Text("Step 3: Rotate (U)", font_size=32).to_edge(UP)
        label_step3.add_background_rectangle()

        self.play(
            ReplacementTransform(label_step2, label_step3),
            ApplyMatrix(U, vector_space),
            run_time=2
        )
        self.wait(1)

        # Final wait
        self.play(FadeOut(label_step3))
        self.wait(1)