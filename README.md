# TableVoos_DynamoLambda
Exercício do LinuxTips de DynamoDB com Lambda, para aplicar conhecimento sobre serviço Lambda da AWS.

## Enunciado
Definição:
Python, usando boto3
DynamoDB

Essa lambda function, deve ser capaz de gravar e ler informações no dynamodb.
No dynamodb, crie uma tabela para armazenar informações de companhia aérea:

* Table: flights
* Items: id, aircraft_prefix, pilot_name, max_load, route

Exemplo do documento:
{id: AA962, aircraft_prefix: N930NN, pilot_name: 'Deep, Jhon', max_load: 136.9, route: GRU-DFW}

Funções: 
1. Crie uma lambda function para criar itens nessa tabela de flights. 
2. Crie uma lambda function para listar todos as informações de voos.
3. Crie uma lambda function para listar informações de um flight id especifico. 

