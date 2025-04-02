say you're on windows and you're tired of going into your python ide to open the application, theres an alternative.

downsides:
* takes significantly more storage, this went from a 1 kb file to a 29.6 MB file for me, this is because it essentially has to replicate a python environment to run from what I've interpreted.
* Takes a little bit of command prompt knowledge, however, not much.

Pros:
*you can now run it from your desktop/wherever you put the executable without having to open a code editor to run it.
*it's cooler
*you should do it anyways unless your poor and dont have 30 MB of space

how to do it:
1. open your command prompt. Im not sure if it works in powershell but I did it in command prompt and it worked so do that just to be safe.
2. navigate to whatever directory the source code is in maybe a folder or downloads if you never moved it etc.
3. type "py -m pip install PyInstaller" in your command prompt (don't include the quotations just type what is in the quotes into your command prompt
4. now type "py -m PyInstaller distance_converter.py --onefile --noconsole --windowed" in the command prompt once it finishes installing. Also without quotes.
5. once that is donw there should be a folder called dist in the directory your in. Inside it will be the executable file.

you can replace distance_converter.py with whatever python file you want to make an executable in the future.
The only reason I didn't upload the executable here is because it exceeded 25 MB and github wont let me upload files bigger than that
