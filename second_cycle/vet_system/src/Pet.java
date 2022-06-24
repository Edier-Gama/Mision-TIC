public class Pet {

    private Integer code;
    private String name;
    private Integer bornYear;
    private String color;
    private String healthStatus;

    public void Eat(){

    }
    public void Move(){

    }

    public void Sound(){

    }

    public void setName(String name){this.name = name;}
    public String getName(){
        return this.name;
    }


    public void setColor(String color) {
        this.color = color;
    }
    public String getColor(String color){
        return this.color;
    }


    public Integer getCode() {
        return code;
    }
    public void setCode(Integer code) {
        this.code = code;
    }


    public Integer getBornYear() {
        return bornYear;
    }
    public void setBornYear(Integer bornYear) {
        this.bornYear = bornYear;
    }


    public String getHealthStatus() {
        return healthStatus;
    }
    public void setHealthStatus(String healthStatus) {
        this.healthStatus = healthStatus;
    }


    public String getFullPet(){
        return "Su mascota se llama " + this.name
                + " nació en el año " + this.bornYear
                + " y está " + this.healthStatus + " de salud";

    }
}
