db.createCollection("usuario", {
    validator : {
        bsonType: "object",
        required: ["login", "senha", "data_criacao", "excluido"],
        properties: {
            login: {
                bsonType: "string",
                minLength: 3,
                maxLenght: 20,
                description: "login inválido"
            },
            senha: {
                bsonType: "string",
                minLength: 5,
                maxLength: 50,
                description: "senha inválida"
            },
            data_criacao: {
                bsonType: "timestamp",
                description: "informe a data de criação do registro"
            },
            alterado_em: {
                bsonType: "timestamp"
            },
            excluido: {
                bsonType: "bool",
                description: "informe se o registro é excluido"
            }
        }
    }
})