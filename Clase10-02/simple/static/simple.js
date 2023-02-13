const firstNameInput = document.getElementById("firstName");
const lastNameInput = document.getElementById("lastName");

const firstNameError = document.getElementById("firstNameError");
const lastNameError = document.getElementById("lastNameError");

const greetButton = document.getElementById("greetButton");

async function greet(firstName, lastName) {

    const body = {
        firstName,
        lastName
    };

    const response = await fetch("http://127.0.0.1:5000/greet", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(body),
    });

    const json = await response.json();

    if (json.answer == "ok") {
        return json.message;
    } else {
        throw json.errors;
    }

    async function onGreetButtonClicked() {
        const firstName = firstNameInput.value;
        const lastName = lastNameInput.value;

        try {
            const message = await greet(firstName, lastName);
            firstNameError.innerText = "";
            lastNameError.innerText = "";
            alert(message);
        } catch (errors) {
            if (errors.firstName) {
                firstNameError.innerText = errors.firstName;
            } else {
                firstNameError.innerText = "";
            }
            if (errors.lastName) {
                lastNameError.innerText = errors.lastName;
            } else {
                lastNameError.innerText = "";
            }
        }
    }
}

    greetButton.addEventListener("click", onGreetButtonClicked);
    
