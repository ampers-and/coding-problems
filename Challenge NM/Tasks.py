if c.charCodeAt(0) >= 65 && c.charCodeAt(0) <= 90{  // please fix condition
        return 'upper';
    } else if c.charCodeAt(0) >= 97 && c.charCodeAt(0) <= 122 {  // please fix condition
        return 'lower';
    } else if c.charCodeAt(0) >= 48 && c.charCodeAt(0) <= 57{  // please fix condition
        return 'digit';
    } else {
        return "other";
    }