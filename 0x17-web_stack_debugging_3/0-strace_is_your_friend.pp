# fixing Apache 500 error .
exec { 'delp':
command  => "sed -i -e 's/.phpp/.php/g' /var/www/html/wp-settings.php",
provider => 'shell',
}
