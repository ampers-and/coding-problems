if c.charCodeAt(0) >= 65 && c.charCodeAt(0) <= 90{  // please fix condition
        return 'upper';
    } else if c.charCodeAt(0) >= 97 && c.charCodeAt(0) <= 122 {  // please fix condition
        return 'lower';
    } else if c.charCodeAt(0) >= 48 && c.charCodeAt(0) <= 57{  // please fix condition
        return 'digit';
    } else {
        return "other";
    }

    map = {"2":["a", "b", "c"], "3":["d","e","f"], "4":["g","h","i"], "5":["j","k","l"], "6":["m","n","o"], "7":["p","q","r","s"], "8":["t","u","v"],"9":["w","x","y","z"]}