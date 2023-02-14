//  Course class used for the Interface

import java.util.*;

public class Course {
    //  Private variables
    private List<String> attribute_list = new ArrayList<String>();
    private String name, discipline, term, block_requirement_id;
    private int credit, number;
    private boolean pass;

    private List<String> prerequisite_list = new ArrayList<String>();

    //  Constructor
    public Course(List<String> attribute_list, boolean pass, String name, int credit, 
                String discipline, int number, String term, String block_requirement_id)
    {
        setAttributeList(attribute_list);
        setPass(pass);
        setName(name);
        setCredit(credit);
        setDiscipline(discipline);
        setNumber(number);
        setTerm(term);
        setBlockRequirementId(block_requirement_id);
    }

    //  Accessors & Mutators
    public void setAttributeList(List<String> attribute_list) {
        this.attribute_list = new ArrayList<String>(attribute_list);
    }
    public List<String> getAttributeList() {
        return attribute_list;
    }

    public void setPass(boolean pass) {
        this.pass = pass;
    }
    public boolean getPass() {
        return pass;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getName() {
        return name;
    }

    public void setCredit(int credit) {
        this.credit = credit;
    }
    public int getCredit() {
        return credit;
    }

    public void setDiscipline(String discipline) {
        this.discipline = discipline;
    }
    public String getDiscipline() {
        return discipline;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public int getNumber() {
        return number;
    }

    public void setTerm(String term) {
        this.term = term;
    }
    public String getTerm() {
        return term;
    }

    public void setBlockRequirementId(String block_requirement_id) {
        this.block_requirement_id = block_requirement_id;
    }
    public String getBlockRequirementId() {
        return block_requirement_id;
    }

    //  Append a prerequisite course to a list
    void addReq(Course c) {
        this.prerequisite_list.add(c.name);
    }

    //  toString for easy printing
    public String toString() {
        return(getDiscipline() + "\t" + getNumber()  + "\t" + getCredit()  + "\t" + getName()  + "\t" + getPass());
    }
}
