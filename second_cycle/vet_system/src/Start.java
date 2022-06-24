public class Start {

    public static void main(String[] args){

        Pet tina = new Pet();

        tina.setName("Tina");
        tina.setCode(01);
        tina.setBornYear(2019);
        tina.setHealthStatus("en buen estado");
        tina.setColor("Amarilla");

        Pet rocke = new Pet();

        rocke.setName("Rocke");
        rocke.setCode(02);
        rocke.setBornYear(2020);
        rocke.setHealthStatus("arañado pero lindo, tiene un buen estado");
        rocke.setColor("Atigrado");

        System.out.println(tina.getFullPet());
        System.out.println(rocke.getFullPet());
    }
}
