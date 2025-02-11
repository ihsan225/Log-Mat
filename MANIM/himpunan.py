from manim import *

class SetHimpunan(Scene):
    def construct(self):
        
        # 1. enumerasi
        title  = Text('ENUMERASI')
        title.to_edge(UP)
        
        set_A  = Text('A={1,2,3,4}')
        set_B  = Text('B={2,4,6,8,10}')
        set_C  = Text('C={1,2,...,100}')
        
        VGroup(title, set_A, set_B, set_C).arrange(DOWN, center=True)
        
        set_A.next_to(title, DOWN, aligned_edge=LEFT)  
        set_B.next_to(set_A, DOWN, aligned_edge=LEFT)  
        set_C.next_to(set_B, DOWN, aligned_edge=LEFT)

        self.play(Write(title))
        self.play(Write(set_A))
        self.play(Write(set_B))
        self.play(Write(set_C))
        self.wait(5)
        
        self.play(FadeOut(Group(title, set_A, set_B, set_C)))
        
        
        # keanggotaan
        judul  = Text('Keanggotaan')
        judul.to_edge(UP)
        
        set_one   = Text('A={1,2,3}, R={a,b,{a,b,c}}')
        set_two   = Text('maka :')
        set_three = Text('3 ∈ A')
        set_four  = Text('{a, b, c} ∈ R')
        
        VGroup(judul, set_one, set_two, set_three).arrange(DOWN, center=True)
        
        set_one.move_to(ORIGIN)
        set_two.next_to(set_one, DOWN).align_to(set_one, LEFT)
        set_three.next_to(set_two, DOWN).align_to(set_one, LEFT)
        set_four.next_to(set_three, DOWN).align_to(set_one, LEFT)

        self.play(Write(judul))
        self.play(Write(set_one))
        self.play(Write(set_two))
        self.play(Write(set_three))
        self.play(Write(set_four))
        self.wait(5)
        
        self.play(FadeOut(Group(judul, set_one, set_two, set_three, set_four)))
        
        
        # 2. diagram venn
        circle_A = Circle(radius=1.5, color=PINK, fill_opacity=0.6)
        circle_B = Circle(radius=1.5, color=YELLOW, fill_opacity=0.6)

        circle_A.shift(LEFT)
        circle_B.shift(RIGHT)

        self.play(Create(circle_A), Create(circle_B))
        self.wait(1)

        universe_label = Tex("U = \\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\\}", color=WHITE)
        universe_label.to_edge(LEFT).to_edge(UP)
        himp_A_label = Tex("A = \\{1, 2, 3, 4, 6\\}", color=WHITE)
        himp_A_label.next_to(universe_label, DOWN)
        himp_B_label = Tex("B = \\{3, 4, 7, 8, 10\\}", color=WHITE)
        himp_B_label.next_to(himp_A_label, DOWN)
        
        self.play(Create(himp_A_label), Create(himp_B_label))
        self.wait(1)

        self.play(Create(universe_label))
        self.wait(1)

        # anggota himpunan A di dalam lingkaran A
        elem_label_A1 = Tex("1", color=WHITE).scale(0.7)
        elem_label_A1.move_to(circle_A.get_center() + UP * 0.5)
        self.play(Create(elem_label_A1))
        self.wait(0.5)

        elem_label_A2 = Tex("2", color=WHITE).scale(0.7)
        elem_label_A2.move_to(circle_A.get_center())
        self.play(Create(elem_label_A2))
        self.wait(0.5)

        elem_label_A3 = Tex("6", color=WHITE).scale(0.7)
        elem_label_A3.move_to(circle_A.get_center() + DOWN * 0.5)
        self.play(Create(elem_label_A3))
        self.wait(0.5)

        # anggota himpunan B di dalam lingkaran B
        elem_label_B1 = Tex("7", color=WHITE).scale(0.7)
        elem_label_B1.move_to(circle_B.get_center() + UP * 0.5)
        self.play(Create(elem_label_B1))
        self.wait(0.5)

        elem_label_B2 = Tex("8", color=WHITE).scale(0.7)
        elem_label_B2.move_to(circle_B.get_center())
        self.play(Create(elem_label_B2))
        self.wait(0.5)

        elem_label_B3 = Tex("10", color=WHITE).scale(0.7)
        elem_label_B3.move_to(circle_B.get_center() + DOWN * 0.5)
        self.play(Create(elem_label_B3))
        self.wait(0.5)

        # anggota himpunan yang ada di antara A dan B
        elem_label_3 = Tex("3", color=WHITE).scale(0.7)
        elem_label_3.move_to((circle_A.get_center() + circle_B.get_center()) / 2 + UP * 0.5)
        self.play(Create(elem_label_3))
        self.wait(0.5)

        elem_label_4 = Tex("4", color=WHITE).scale(0.7)
        elem_label_4.move_to((circle_A.get_center() + circle_B.get_center()) / 2 + DOWN * 0.5)
        self.play(Create(elem_label_4))
        self.wait(0.5)

        # anggota himpunan yang ada di luar A dan B
        elem_label_5 = Tex("5", color=WHITE).scale(0.7)
        elem_label_5.move_to(RIGHT * 2 + UP * 1.5)
        self.play(Create(elem_label_5))
        self.wait(0.5)

        self.play(
            FadeOut(Group(universe_label, himp_A_label, himp_B_label, circle_A, circle_B, elem_label_A1, elem_label_A2, elem_label_A3,
                          elem_label_B1, elem_label_B2, elem_label_B3, elem_label_3, elem_label_4, elem_label_5))
        )
        self.wait(1)
        
if __name__ == "__main__":
    scene = SetHimpunan()
    scene.render()