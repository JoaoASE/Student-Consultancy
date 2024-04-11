import pandas as pd

dados = pd.read_excel("Alunos repetidos unidades.xlsx")

qtd_matriculas = []
for index, row in dados.iterrows():
  id_aluno = row['Aluno']
  cursos = row['Curso']
  unidade = row['Unidade']  
  for curso in cursos.split(
      ', '): 
    mat = {'id_aluno': id_aluno, 'id_curso': curso, 'Unidade': unidade}
    qtd_matriculas.append(mat)

matriculas = pd.DataFrame(qtd_matriculas)


alunos_repetidos_por_unidade = matriculas.groupby(
    ['Unidade', 'id_aluno']).size().reset_index(name='count')
alunos_repetidos_por_unidade = alunos_repetidos_por_unidade.groupby(
    'Unidade').apply(lambda x: (x['count'] > 1).sum())

print("Unidades com alunos matriculados em mais de um curso:")
print(alunos_repetidos_por_unidade[alunos_repetidos_por_unidade > 0])
