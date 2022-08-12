import pandas as pd

data = pd.read_csv("E:/Git/Задания tasks/Tasks1/adult.data.csv", sep=',')
data.head()

print(pd.DataFrame(data), '\n')

value_counts = data['sex'].value_counts()
print('Кол-во муж. и жен. в датасете: ''\n', value_counts, '\n')  # кол-во муж. и жен. в датасете

age_male = data.loc[data["sex"] == "Male", "age"].mean()
print('Средний возраст мужчин: ', age_male, '\n')  # средний возраст Male

share = data['native-country'].str.contains('United-States').mean()  # доля граждан Соединенных Штатов
print('Доля граждан Соединенных Штатов: ', share, '\n')

sum_b = data.groupby("salary")["age"].mean()  # среднее значение кто получает > и <= 50K в год
print('Среднее значение кто получает <= и > 50K в год:''\n', sum_b, '\n')

deviation = data.groupby("salary")["age"].std()  # среднеквадратичное отклонение кто получает <= и > 50K в год
print('Среднеквадратичное отклонение кто получает <= и > 50K в год:''\n', deviation, '\n')

all_records = data[data['salary'] == '>50K']['education'].count()  # число всех записей
education = data.loc[data['salary'] == '>50K', 'education'].value_counts()  # образование всех людей > 50
print('Колличество людей c прибылью > 50K: ', all_records, '\n', 'Образование:', '\n', education, '\n')
all_records = data.loc[data['salary'] == '>50K', 'education'].isin(
    ['Bachelors', 'Prof-school', 'Assoc-acdm', 'Assoc-voc', 'Masters', 'Doctorate']).value_counts().to_frame()
print('True Колличество людей с высшим образованием: ', '\n', all_records, '\n')

for (race, sex), i in data.groupby(['race', 'sex']):  # Вывод статистики возраста для каждой расы и каждого пола
    print('\n', 'Национальность', race, 'Пол', sex)
    print(i['age'].describe(), '\n')

all_married = [i for i in data['marital-status'].unique() if i.startswith('Married')]
married = data[(data['sex'] == 'Male') & (data['marital-status'].isin(all_married))]['salary'].value_counts()
not_married = data[(data['sex'] == 'Male') & (~data['marital-status'].isin(all_married))]['salary'].value_counts()
print('Колличество женатых после 50: ', married[1])
print('Колличество не женатых после 50: ', not_married[1])
print("Доля заработка среди женатых %: ", married[1] * 100 / (married[1] + not_married[1]))
print("Доля заработка среди не женатых %: ", not_married[1] * 100 / (not_married[1] + married[1]), '\n')

max_week_work = data['hours-per-week'].max()
print("Максимальное число часов человек работает в неделю: ", max_week_work)
people_time_max = data.loc[data['hours-per-week'] == max_week_work].shape[0]
print("Колличество людей с максимальным числом работы в неделю: ", people_time_max)
much_money = 100 * data[(data['hours-per-week'] == max_week_work) & (data['salary'] == '>50K')].shape[
    0] / people_time_max
print("Процент среди них зарабатывающих много: ", much_money, '\n')

for (country, salary), i in data.groupby(['native-country', 'salary']):
    print(country, salary, i['hours-per-week'].mean())


def AgeFroup(x):  # присваем значение в новую колонку AgeFroup
    if x >= 16 and x <= 35:
        return 'young'
    elif x > 35 and x <= 70:
        return 'adult'
    elif x > 70 and x <= 100:
        return 'retiree'


data["AgeGroup"] = data['age'].apply(AgeFroup)  # создаем новую колонку AgeFroup
print(data, '\n')

value_group = data['AgeGroup'].value_counts().reset_index()  # вывод колличества людей каждой группе в колонке AgeGroup
print('Кол-во людей в каждой группе AgeGroup: ''\n', value_group, '\n')

salary_group = data.loc[
    data["salary"] == ">50K", "AgeGroup"].value_counts().reset_index()  # вывод дохода > 50K в каждой группе
print('Количество людей по каждой группе доход свыше 50K: ', '\n', salary_group, '\n')
print("Название возрастной группы, в которой чаще зарабатывают больше 50К (>50K):", '\n', salary_group.max(), '\n')

group_people = data.sort_values('occupation', ascending=False)  # Группируем по стобцу occupation
print(group_people)
"""print(pd.set_option('display.max_columns', None), group_people)
можно вывести все строки таблицы для сверки правильности группировки столбца occupation """
count_people_group = data.groupby(['occupation'])['age'].count()  # Вывод кол-ва людей по каждой группе
print(count_people_group)

filter_func = data.groupby('occupation').agg({'age': ['mean'], 'hours-per-week': ['min']})
print(filter_func)  # группировка по occupation где найден средний созраст и минимальное время в неделю
filter_func = filter_func[(filter_func['age']['mean'] < 40) & (filter_func['hours-per-week']['min'] > 5)]
print(filter_func)  # вывод группы где средний возраст меньше 40 лет и отработано больше 5 часов в неделю
