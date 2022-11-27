import java.util.regex.*;
import java.util.Scanner;
 
class Regex{
     
public static boolean isValid(String s)
{
     
    
    Pattern p = Pattern.compile("[+]?[1]?[\\-(\\s]?[1-9]{3}[)\\s\\-\\.]{0,2}[0-9]{3}[\\-\\.\\s][0-9]{4}");
 
    Matcher m = p.matcher(s);
    return (m.find() && m.group().equals(s));
}
 
public static void main(String[] args)
{
    //we can un-comment and check validity for either of the numbers
	String s = "1-212-456-7890";
//	String s = "212-456-7890";
//	String s = "(212)456-7890";
//	String s = "(212)-456-7890";
//	String s = "212.456.7890";
//	String s = "212 456 7890";
//	String s = "+12124567890";
//	String s = "+1 212.456.7890";
//	String s = "+212-456-7890";
//		     
    if (isValid(s))
        System.out.println("Valid Number");    
    else
        System.out.println("Invalid Number");    
}
}
