import numpy as np

arr = np.arange(11)
arr[(arr > 3) & (arr < 8)] *= -1
print(arr, '\n')

arr2 = np.random.random((10,))
print(arr2)
arr2[np.argmax(arr2)] = 0
print(arr2, '\n')

arr3 = np.array([1, 2, 3])
arr4 = np.array([4, 5, 6])
arr_m = np.array([(i, j) for i in arr3 for j in arr4])
print(arr_m, '\n')



arr5 = np.random.randint(0, 2, (10, 3))
print(arr5)
arr_del = arr5[~np.logical_and.reduce(arr5[:, 1:] == arr5[:, :-1], axis=1)]
print(arr_del, '\n')

arr9 = np.array([[1, 2, 3], [1, 2, 3], [2, 3, 4], [2, 3, 4], [4, 5, 6]])
arr_uniq = np.unique(arr9, axis=0)
print(arr9, '\n')
print(arr_uniq, '\n')

''' Для каждой из следующих задач (1-5) нужно привести 2 реализации – одна без использования numpy (cчитайте, 
что там, где на входе или выходе должны быть numpy array, будут просто списки), а вторая полностью 
векторизованная с использованием numpy (без использования питоновских циклов/map/list comprehension). '''

p = np.array([[1, 0, 1], [2, 0, 2], [3, 0, 3], [4, 4, 4]])
p = np.diag(p)
print(np.prod(p[p != 0]))

A = [[1, 0, 1], [2, 0, 2], [3, 0, 3], [4, 4, 4]]
s = 1
for i in range(len(A)):
    for j in range(len(A[i])):
        if A[i] == A[j] and A[i][j] > 0:
            s *= A[i][j]
print(s, '\n')

x = np.array([1, 2, 2, 4])
y = np.array([4, 2, 1, 2])
print(x in y)

x1 = ([1, 2, 2, 4])
y1 = ([4, 2, 1, 2])
print(set(x1) == set(y1), '\n')

x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
x_m = x == 0
print(max(x[1:][x_m[:-1]]))

x1 = [6, 2, 0, 3, 0, 0, 5, 7, 0]
s = 0
for i in range(len(x1) - 1):
    if x1[i] == 0 and x1[i + 1] > s:
        s = x1[i + 1]
print(s, '\n')

x = np.array([2, 2, 2, 3, 3, 3, 5])
unique_chars, char_counts = np.unique(x, return_counts=True)
print(list(unique_chars))
print(list(char_counts), '\n')

x1 = [2, 2, 2, 3, 3, 3, 5]
print(list(set(x1)))
print([(x1.count(i)) for i in set(x1)], '\n')

import scipy.spatial.distance

x1 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
x2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
t = scipy.spatial.distance.cdist(x1, x2)
print(scipy.spatial.distance.cdist(x1, x2))

x1 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
x2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
P = np.add.outer(np.sum(x1 ** 2, axis=1), np.sum(x2 ** 2, axis=1))
print(np.sqrt(P - 2 * (np.dot(x1, x2.T))))

''' Вы работаете в отделе маркетинга пищевой компании MyCrunch, которая разрабатывает новый вид вкусных,полезных 
злаков под названием CrunchieMunchies.

Вы хотите продемонстрировать потребителям, насколько полезны ваши хлопья по сравнению с другими ведущими 
брендами, поэтому вы собрали данные о питании нескольких разных конкурентов.

Ваша задача - использовать вычисления Numpy для анализа этих данных и доказать, что 
ваши СrunchieMunchies - самый здоровый выбор для потребителей. '''

calorie_stats = np.loadtxt("E:\Git\Задания tasks\Tasks1\cereal.csv", delimiter=",")
print(calorie_stats, '\n')  # Вывод списка

average_calories = np.average(calorie_stats)
print(average_calories, 'Вывод среднего значения калорий', '\n')  # Вывод среднего значения калорий

calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted, 'Сортируем список по возрастанию', '\n')  # Сортируем список по возрастанию

median_calories = np.median(calorie_stats)
print(median_calories, 'Вывод медианы', '\n')  # Вывод медианы

nth_percentile = np.percentile(calorie_stats, 4)  # минимальный процентили превышающий 60
print(nth_percentile, 'минимальный процентили превышающий 60', '\n')

more_calories = len(calorie_stats[(calorie_stats > 60)]) * 100 / len(calorie_stats)  # процент массива после 60
print(more_calories, 'процент массива после 60', '\n')

calorie_std = np.std(calorie_stats)  # стандартное отклонение массива
print(calorie_std, 'стандартное отклонение', '\n')

print('CrunchieMunchies - это продукт, который пзволит уталить чувтсво голода, и получить прилив энергии и сил')
