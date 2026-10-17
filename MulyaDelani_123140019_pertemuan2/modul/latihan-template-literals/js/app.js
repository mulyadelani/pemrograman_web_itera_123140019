(() => {
function demoVariables() {
  function getVarValue() {
    if (true) {
      var oldVar = "tetap dapat diakses setelah block";
    }
    return oldVar;
  }

  function getLetValue() {
    let newLet;
    {
      let blockScoped = "hanya tersedia dalam block tempat dideklarasikan";
      newLet = blockScoped;
    }
    return newLet;
  }

  const PI = 3.14159;
  const user = { name: "Mulya Delani" };
  user.name = "Mulya Delani (objek const dapat diperbarui)";

  return {
    oldVar: getVarValue(),
    newLet: getLetValue(),
    PI,
    user,
  };
}

function demoArrowFunctions() {
  function regularSum(first, second) {
    return first + second;
  }

  const arrowSum = (first, second) => first + second;
  const shortArrowSum = (first, second) => first + second;
  const sayHello = () => "Halo, Mulya!";
  const square = (number) => number ** 2;

  return {
    regularSum: regularSum(4, 6),
    arrowSum: arrowSum(4, 6),
    shortArrowSum: shortArrowSum(4, 6),
    sayHello: sayHello(),
    square: square(5),
  };
}

function demoTemplateLiterals() {
  const name = "John";
  const age = 30;
  const birthYear = new Date().getFullYear() - age;
  const oldWay = "Nama saya " + name + " dan umur saya " + age + " tahun.";
  const newWay = `Nama saya ${name} dan umur saya ${age} tahun.`;
  const multiLine = `
    <article class="student-card">
      <h2>Halo, ${name}!</h2>
      <p>Selamat belajar JavaScript ES6+.</p>
      <p>Umur: ${age} tahun · Tahun lahir: ${birthYear}</p>
    </article>
  `;
  const expression = `Perkiraan tahun lahir: ${new Date().getFullYear()} - ${age} = ${birthYear}`;

  return { oldWay, newWay, multiLine, expression };
}

window.BloomStudyDemos = {
  demoVariables,
  demoArrowFunctions,
  demoTemplateLiterals,
};
})();
