# V.I.M.M - Aplicativo de Agenda

# P.P.a.R (Principal Problema a ser Resolvido) 
- O estudante **não tem a responsabilidade** de entregar e/ou cumprir com suas obrigações escolares no prazo.
- Docentes tendo que constantemente **relembrar seus alunos de realizarem suas tarefas** e/ou marcar provas em dias de falta.

# R.F (Requisitos Funcionais)
- **Autenticação:** O aplicativo deve permitir que os usuários façam login e se registrem como Professor ou Aluno.
- **Visualização de Calendário:** O aplicativo deve exibir um calendário semanal para o usuário, mostrando quaisquer pendências ou compromissos escolares.
- **Alertas de Tarefas:** O aplicativo deve fornecer alertas visuais para tarefas pendentes, com cores diferentes para indicar a urgência da tarefa.
- **Navegação no Calendário:** Os usuários devem ser capazes de expandir o calendário para visualizar todo o mês e navegar entre os meses.
- **Menu de Navegação:** O aplicativo deve fornecer um menu com opções para “Turmas que Participo”, “Notas Atribuídas”, “Configurações” e “Sair”.
- **Perfil do Usuário:** O aplicativo deve permitir que os usuários acessem e personalizem seu perfil.
- **Criação de Tarefas/Compromissos:** O aplicativo deve permitir que os alunos adicionem tarefas ou compromissos à sua agenda de forma manual.

# R.N.F (Requisitos Não Funcionais)
- **Usabilidade:** O aplicativo deve ser fácil de usar, com uma interface intuitiva e amigável.
- **Desempenho:** O aplicativo deve responder rapidamente às ações do usuário e não deve ter atrasos perceptíveis.
- **Segurança:** Os dados do usuário, incluindo informações de login e notas, devem ser armazenados de forma segura.
- **Compatibilidade:** O aplicativo deve ser compatível com as versões mais recentes dos sistemas operacionais móveis.
- **Confiabilidade:** O aplicativo deve ser confiável e consistente em seu desempenho, sem falhas ou erros frequentes.
- **Disponibilidade:** O aplicativo deve estar disponível para uso a qualquer momento, a menos que esteja em manutenção programada.
- **Escalabilidade:** O aplicativo deve ser capaz de lidar com um grande número de usuários simultâneos sem degradação do desempenho.

# Protótipo 
- Ao acessar o Aplicativo, o usuário irá se deparar com uma tela de **Login** e (se não possuir uma conta) **Sign-In**. O Aplicativo oferecerá a capacidade de **Logar** como Professor ou Aluno. Ao entrar, o usuário **Aluno** verá um caledário de sua semana no meio da tela, neste, constará se usuário possui alguma pendência ou compromisso escolar naquele dia/semana. Se houver, um sinal de alerta aparecerá em cima do dia em questão, tarefas com prazo restante de *14+ dias* terão alertas de cor **Amarela**, de *7+ dias* cor **Laranja** e tarefas com *menos de uma semana* de prazo, mostrarão um sinal de alerta de cor **Vermelha**. O usuário terá a opção de expandir esse calendário, mostrando todos os dias do mês, e podendo também, navegar entre os meses do ano.
- Ao entrar como **Professor**, o usuário também terá as mesmas funcionalidades da *"Versão Aluno"*, com o adicioanl de algumas implementações. Como Professor, você poderá criar **Turmas**, **Atribuir Tarefas** à esta turma, **Agendar Provas** e **Enviar Lembretes aos seus Alunos**. 
- No canto superior esquerdo, o aplicativo mostrará **Três Linhas** de Menu, que ao ser pressionada, apresentará as opções: **Turmas que Participo**, **Notas Atribuídas**, **Configurações** e **Sair**. No canto superior direito, teremos uma **Bolinha**, representando o perfil do usuário, consequentemente, quando pressionado, levará o usuário a seu próprio perfil, tendo a opção de personalizá=lo.
- Abaixo do calendário, terá também a opção de **Criar Nova Tarefa/Compromisso**, caso o aluno queira colocar algo em sua agenda, de forma manual. Lembremos que, ao estar em uma turma, o aluno estará submetido as tarefas/compromissos adicionadas pelo seu professor. No Meio Superior da Tela, a logo do aplicativo.

# Fluxograma 

# Tela Inicial do Aplicativo:

![image](https://github.com/lucaspatracao/V.I.M.M/assets/166610416/15ae7d8e-732d-44b0-889f-cf1815df4234)

# Opção de Adicionar Tarefas:

![image](https://github.com/lucaspatracao/V.I.M.M/assets/166610416/dc4a6f33-af21-4ac2-a844-d38c12e0b825)

