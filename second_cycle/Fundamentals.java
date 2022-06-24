public class Fundamentals {

    public static void main(String[] args) {

        /*A Variable can start with $ or _ but in java is very common to see
	  lowerCamelCase on this*/

        //In java +10 version we can use VAR

        /*---------------------------------------------------------------------------------*/

        var $name = "Edier";
        $name = $name + " Santiago";
        var surname = "Gama";
        surname = surname + " Cusguen";
        var age = 17;

        var sentence = ("My name is: " + $name + " " + surname + " and I'm " + age + " years old :D");

        System.out.println(sentence);

        //CONSTANTS VALUES

        var PI = (long) 3.1416;
        //System.out.println(PI);

        /*---------------------------------------------------------------------------------*/

        //Integer values only can use 10 numbers max

        Integer numbers = 1234567890; // +1 it's an error

        //Float is for inexactly values +4.
        //Long is for exactly values 1.

        long nL = (long) 4.765;
        float nF = 1.345f;

        //Booleans true or false

        boolean isTrue = true;
        boolean isFalse = false;

        var salary = 1000;
        var pension = 200;
        salary += pension;

        //System.out.println("Hello, my salary is: "+salary);
        /*---------------------------------------------------------------------------------*/

        //Increment and decrement

        var lives = 5;
        lives = lives - 1;
        lives--;
        lives++;
        var gift = 100 + ++lives;

        //System.out.println("I have "+gift+" lives");

        /*---------------------------------------------------------------------------------*/

        //Mathematical operation
        //Math library

        double x = 7.1;
        var y = 3;
        //floor and ceil return the nearest integer
        System.out.println(Math.floor(x));
        System.out.println(Math.ceil(x));

        //pow return the power of x
        System.out.println(Math.pow(x, y));

        //sqrt return the square root of x
        System.out.println(Math.sqrt(x));

        //max and min return the maximum and minimum of x
        System.out.println(Math.max(x, y));
        System.out.println(Math.min(x, y));

        //radio of circle
        var radio = 5;
        System.out.println(Math.PI * Math.pow(radio, 2));

        //area of esfera
        System.out.println(4 * Math.PI * Math.pow(radio, 2));

        //volume of esfera
        System.out.println((4 / 3) * Math.PI * Math.pow(radio, 3));

        /*---------------------------------------------------------------------------------*/


        //cast it's for change the type of variable and estimate the value

        var perros = 30;
        var año = (int) (perros / 12);
        System.out.println(año);

        char letra = 'a';
        int letraI = (int) letra;
        System.out.println(letraI);


        //CONDITIONALS

        var edad = 17;
        if (edad == 18) {
            System.out.println("You are older than 18");
        } else {
            System.out.println("You are younger than 18");
        }

        switch (edad) {
            case 18:
                System.out.println("You are older than 18");
                break;
            case 17:
                System.out.println("You are younger than 18");
                break;
            default:
                System.out.println("You are not 18");
                break;
        }
    }
}








