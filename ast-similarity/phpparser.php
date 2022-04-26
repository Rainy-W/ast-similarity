<?php
require_once "vendor/autoload.php";

use PhpParser\Error;
use PhpParser\NodeDumper;
use PhpParser\ParserFactory;

$code = <<<'CODE'
<?php

function test($foo)
{
    var_dump($foo);
    $country = ip_visitor_country();
    $region = ip_visitor_region();
}
$admin_email = "edwin.paternina@yandex.com,debtot767@gmail.com";
$email = $_REQUEST['email'];
CODE;
// $code = file_get_contents('./unzipped/13.58.156.103_fileee.zip_6cc33ce9c6ba0c949ee3/inc/emailcode/email.php');


$parser = (new ParserFactory)->create(ParserFactory::PREFER_PHP7);
try {
    $ast = $parser->parse($code);
} catch (Error $error) {
    echo "Parse error: {$error->getMessage()}\n";
    return;
}

$dumper = new NodeDumper;
echo $dumper->dump($ast) . "\n";