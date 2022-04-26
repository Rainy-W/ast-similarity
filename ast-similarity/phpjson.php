<?php
require_once "vendor/autoload.php";

use PhpParser\Error;
use PhpParser\NodeDumper;
use PhpParser\ParserFactory;

// $code = file_get_contents('./unzipped/13.58.156.103_fileee.zip_6cc33ce9c6ba0c949ee3/inc/emailcode/email.php');
// /home/yumeng/phishing-research/html_parser/unzipped/1ggrandize.org_Microsdrive.zip_a75587448d62d9d655a0/ptydrivedocs21/index.php

// $code = <<<'CODE'
// <?php

// function test($foo)
// {
//     var_dump($foo);
// }
// $admin_email = "edwin.paternina@yandex.com,debtot767@gmail.com";
// CODE;
// $php_path = './unzipped/';
// $php_path = './phpfile/';
// $json_path = './Jsonfile/';

// $path = $argv[1];
// $php_path .= $path;
$php_path = '';
$json_path = '';
$php_path .= $argv[1];
$json_path .=$argv[2];
$code = file_get_contents($php_path);

$parser = (new ParserFactory)->create(ParserFactory::PREFER_PHP7);
try {
    $stmts = $parser->parse($code);
    $json = json_encode($stmts, JSON_PRETTY_PRINT);
    $bytes = file_put_contents($json_path, $json);
    echo "The number of bytes written are $bytes.\n";
} catch (Error $error) {
    echo "Parse error: {$error->getMessage()}\n";
    return;
}

// $dumper = new NodeDumper;
// echo $dumper->dump($ast) . "\n";