db.createCollection("organizacao", {
    validator : {
        $jsonSchema: {
            bsonType: "object",
            required : ["nome", "cnpj", "data_criacao", "excluido"],
            properties: {
                nome: {
                    bsonType: "string",
                    minLength: 3,
                    maxLength: 500,
                    description: "nome inválido"
                },
                cnpj: {
                    bsonType: "string",
                    minLength: 14,
                    maxLength: 14,
                    description: "CNPJ inválido"
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