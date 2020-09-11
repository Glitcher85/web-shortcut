using System;
using System.IO;
using System.Diagnostics;

namespace SaveOpener {
    public class Program {
        static void Main(string[] args) {
            string current_directory = Directory.GetCurrentDirectory();
            string destination = current_directory + @"\programs\save.py";
	    string command = "/c notepad " + destination;
            if (File.Exists(destination)) {
                Process.Start("cmd", command);
            } else {
                Console.WriteLine("[ERROR]: An exception occured.");
		Console.WriteLine("Please make sure to open the main program at least once to create 'save.py' and do not change the directory name.\n");
		Console.WriteLine("Press [ENTER] to exit...");
		Console.ReadLine();
            }
        }
    }
}
