const student = {
  name: "ნინო",
  surname: "გაბუნია",
  academy: "პროგრამირების აკადემია",
  city: "თბილისი",
  role: "მოსწავლე",
  favColor: "ლურჯი",

  fullName: function () {
    console.log(this.name + " " + this.surname);
  },

  showFavColor: function () {
    console.log("საყვარელი ფერი:", this.favColor);
  }
};

// 1. დაბეჭდეთ მთლიანი ობიექტი
console.log(student);

// 2. დაბეჭდეთ ნებისმიერი კუთვნილება
console.log("ქალაქი:", student.city);

// 3. გამოიძახეთ ობიექტის რომელიმე მეთოდი
student.fullName();

// 4. შეცვალეთ ობიექტის რომელიმე მნიშვნელობა
student.favColor = "მწვანე";
console.log("განახლებული საყვარელი ფერი:", student.favColor);