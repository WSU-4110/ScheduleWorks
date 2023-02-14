//  Private info class for login, for testing login

public class privateInfo {
    //  Username and password
    private String username;
    private String password;

    public privateInfo() {
        setUsername("");
        setPassword("");
    }

    protected void setUsername(String username) {
        this.username = username;
    }
    protected String getUsername() {
        return username;
    }
    protected void setPassword(String password) {
        this.password = password;
    }
    protected String getPassword() {
        return password;
    }
}
