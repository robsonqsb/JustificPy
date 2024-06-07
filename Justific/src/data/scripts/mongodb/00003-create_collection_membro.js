db.createCollection("membro", {
    validator : {
        $jsonSchema: {
            bsonType: "object",
            required : ["codigo_registro", "nome", "data_criacao", "excluido"],
            properties: {
                codigo_registro: {
                    bsonType: "string",
                    minLength: 3,
                    maxLength: 50,
                    description: "codigo de registro inválido"
                },
                nome: {
                    bsonType: "string",
                    minLength: 3,
                    maxLength: 500,
                    description: "nome inválido"
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