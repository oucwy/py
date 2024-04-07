// 打印一个数组中的所有元素

interface Person {
  name: string;
  age: number;
}

const people: Person[] = [
  { name: "John", age: 25 },
  { name: "Alice", age: 30 },
  { name: "Bob", age: 35 },
];

for (const person of people) {
  console.log(`Name: ${person.name}, Age: ${person.age}`);
}
