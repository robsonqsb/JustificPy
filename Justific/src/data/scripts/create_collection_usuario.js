db.createCollection("usuario", {
    validator : {
        $jsonSchema:{
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
                    bsonType: "date",
                    description: "informe a data de criação do registro"
                },
                alterado_em: {
                    bsonType: ["date", "null"]
                },
                excluido: {
                    bsonType: "bool",
                    description: "informe se o registro é excluido"
                }
            }
        }
    }
})