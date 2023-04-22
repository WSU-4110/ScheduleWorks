//  Course class used for the Interface
package org.scheduleworks.dep;

import java.util.*;

public class Course {
    //  Private variables
    private List<String> attribute_list = new ArrayList<String>();
    private String name, discipline, term, block_requirement_id;
    private String credit, number;
    private String pass;

    private List<String> prerequisite_list = new ArrayList<String>();

    //  Constructor
    public Course(List<String> attribute_list, String pass, String name, String credit, 
                String discipline, String number, String term, String block_requirement_id)
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
    public Course(String pass, String name, String credit, 
                String discipline, String number)
    {
        setPass(pass);
        setName(name);
        setCredit(credit);
        setDiscipline(discipline);
        setNumber(number);

    }

    //  Accessors & Mutators
    public void setAttributeList(List<String> attribute_list) {
        this.attribute_list = new ArrayList<String>(attribute_list);
    }
    public List<String> getAttributeList() {
        return attribute_list;
    }

    public void setPass(String pass) {
        this.pass = pass;
    }
    public String getPass() {
        return pass;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getName() {
        return name;
    }

    public void setCredit(String credit) {
        this.credit = credit;
    }
    public String getCredit() {
        return credit;
    }

    public void setDiscipline(String discipline) {
        this.discipline = discipline;
    }
    public String getDiscipline() {
        return discipline;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getNumber() {
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

    //  toString for easy prStringing
    public String toString() {
        return(getDiscipline() + "\t" + getNumber()  + "\t" + getCredit()  + "\t" + getName()  + "\t" + getPass());
    }
}
