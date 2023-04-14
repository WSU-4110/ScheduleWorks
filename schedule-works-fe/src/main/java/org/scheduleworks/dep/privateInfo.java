//  Private info class for login & app settings

package org.scheduleworks.dep;

import org.json.JSONException;
import org.json.JSONObject;
import org.json.simple.JSONObject;

public class privateInfo {
    JSONObject loginData = new JSONObject();
    //  Username and password
    private String username;
    private String password;
    //  App settings toggles
    private boolean seleniumToggle;
    private boolean saveCookiesToggle;

    public privateInfo() {
        setUsername("");
        setPassword("");
        setSeleniumToggle(true);
        setSaveCookiesToggle(true);
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

    protected void setSeleniumToggle(boolean seleniumToggle) {
        this.seleniumToggle = seleniumToggle;
    }
    protected boolean getSeleniumToggle() {
        return seleniumToggle;
    }
    protected void setSaveCookiesToggle(boolean saveCookiesToggle) {
        this.saveCookiesToggle = saveCookiesToggle;
    }
    protected boolean getSaveCookiesToggle() {
        return saveCookiesToggle;
    }
}
