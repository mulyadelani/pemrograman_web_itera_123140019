const {
  demoArrowFunctions,
  demoTemplateLiterals,
  demoVariables,
} = window.BloomStudyDemos;

const output = document.querySelector("#output");
const runButton = document.querySelector("#runBtn");

function addOutput(title, description, result) {
  const card = document.createElement("article");
  card.className = "result-card";

  const heading = document.createElement("h3");
  heading.textContent = title;
  const summary = document.createElement("p");
  summary.className = "result-description";
  summary.textContent = description;
  const content = document.createElement("pre");
  content.textContent = result;

  card.append(heading, summary, content);
  output.append(card);
}

function runAllDemos() {
  const varResults = demoVariables();
  addOutput(
    "1. Let dan Const",
    "var vs let/const dan block scope",
    `var (function scope): ${varResults.oldVar}
let (block scope): ${varResults.newLet}
const (nilai tetap): ${varResults.PI}
const object (isi dapat diubah): ${JSON.stringify(varResults.user)}`
  );

  const arrowResults = demoArrowFunctions();
  addOutput(
    "2. Arrow Functions",
    "Perbandingan fungsi reguler dan arrow functions",
    `Regular function: ${arrowResults.regularSum}
Arrow function: ${arrowResults.arrowSum}
Short arrow: ${arrowResults.shortArrowSum}
No params: ${arrowResults.sayHello}
Single param: ${arrowResults.square}`
  );

  const templateResults = demoTemplateLiterals();
  addOutput(
    "3. Template Literals",
    "Concatenation vs interpolasi, string multi-baris, dan ekspresi",
    `Old way: ${templateResults.oldWay}
New way: ${templateResults.newWay}
With expression: ${templateResults.expression}
Multi-line:${templateResults.multiLine}`
  );
}

runButton.addEventListener("click", () => {
  output.replaceChildren();
  runAllDemos();
});
