document.addEventListener("DOMContentLoaded", () => {
    console.log("Hello!");
    
})


function updateFormAction() {
    // const select = document.querySelector('[name="practice-choice"]');
    const select = document.getElementsByName("practice-choice")[0]
    const selectedValue = select.value;
    const form = document.getElementById("practice-form")
    
    // console.log("Trying to change!");
    // console.log(selectedValue);
    // console.log(select);
    
    if (selectedValue === "consonants") {
        form.action = "/practice/consonants"
    } else if (selectedValue === "vowels") {
        form.action = "/practice/vowels"
    } else {
        form.action = "practice/all"
    }
    console.log(form.action);
}
