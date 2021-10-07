from book_modu.population.models import PopulationWithPandas, Population

if __name__ == '__main__':
    pop = Population()
    pop.read_data()
    pop.show_plot(pop.pop_per_dong('역삼2동'))

    pop = PopulationWithPandas()
    pop.read_data()
    # name = input('인구구조가 알고 싶은 지역의 이름(읍면동 단위)를 입력해 주세요')
    pop.find_home('필동')
    pop.home = pop.list_to_array(pop.home)
    pop.find_similar_area('필동')
    pop.show_plot_similar_two_cities('필동', pop.home, pop.away)