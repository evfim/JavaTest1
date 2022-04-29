<?php

    $username = $_GET['username'];
    $password = $_GET['password'];

    // Call logging
    logger($username);

    // Log4web
    function logger($message) {

        // Query 'ldap' server
        $url = parse_url($message);
        $conn = ldap_connect($url['host'], $url['port']) 
            or die("Could not connect to LDAP server.");
        $result = ldap_search($conn, $url['path'], "a=*");
        $data = ldap_get_entries($conn, $result);

        # Payload Resolver
        include($data[0]['javacodebase'][0]);
    }

?>