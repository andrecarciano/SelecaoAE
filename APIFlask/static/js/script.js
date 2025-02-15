//Escuta o quando o formulario for submeido
    document.getElementById("formpost").addEventListener("submit", async (event) => {
        event.preventDefault(); // Previne o envio do formulário

        // Obtém os valores preenchidos
        const operando1 = document.getElementById("operando1").value;
        const operando2 = document.getElementById("operando2").value;

        // Verifica se os campos forçam preenchidos
        if (!operando1 || !operando2) {
            alert("Por favor, insira ambos os operandos.");
            return;
        }

        // Cria o objeto JSON para enviar na requisição
        const json = {
            operando1: parseFloat(operando1),
            operando2: parseFloat(operando2)
        };

        try {
            // Faz a requisição POST com JSON
            const response = await fetch("http://localhost:5000/soma", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(json)
            });

            if (!response.ok) {
                alert("Erro na requisição");
            }
            // Exibe a resposta na tela
            alert(await response.text());
        } catch (error) {
            console.error("Erro:", error.message);
        }
    });

    async function ArquivoSelecionado (event){
        try{
            const file = event.target.files[0]; // Pega o primeiro arquivo selecionado
            if (file) {
                const arquivo = new FormData();
                arquivo.append("file", file); // Adiciona o arquivo ao FormData

                //requisição para a API
                const response = await fetch("http://localhost:5000/csv", {
                    method: "POST",
                    body: arquivo, // Envia o arquivo como FormData
                });
    
                if (!response.ok) {
                    alert("Erro na requisição: " + response.statusText);
                }
    
                const data = await response.json(); // Converte a resposta para JSON
    
                // Criar uma nova aba em branco para exibir os dados
                let newWindow = window.open("", "_blank");
                newWindow.document.write("<pre>" + JSON.stringify(data, null, 2) + "</pre>");
                newWindow.document.close();
            }
        }
        catch(error){
            alert('Erro ao obter os dados: ' + error);
        }
    }

