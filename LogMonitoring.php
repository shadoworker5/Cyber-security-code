<?php
/*
* @author Shadoworker5 Dev
* @email shadoworker5.dev@gmail.com
* @create date 2023-01-11 23:05:29
* @modify date 2023-07-04 10:47:06
* @desc [description]
*/

class LogMonitoring {
    private static $support_address        = 'example@example.xyz';
    private static $mail_subject           = 'An Exception occur in your application';
    private static $slack_bot_url          = 'https://hooks.slack.com/services/XXXXXXXXX/XXXXXXXXX/XXXXXXXXXXXXXXXXXX';
    private static $discord_webhooks_url   = 'https://discordapp.com/api/webhooks/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX';

    public static function sendByMail($content) {
        try {
            $message = 'Hi. Something went wrong in your application. Some detail here: '. json_encode($content);
            mail(self::$support_address, self::$mail_subject, $message);
        } catch (Exception $e) {
            self::sendBySlack($content);
            self::sendBySlack('Error sendByMail: '.json_encode($e));
        }
    }

    public static function sendBySlack($content) {
        try {
            $query_init_curl    = curl_init();
            $header             = ['Content-Type: application'];
            $query_data         = "{'text': '$content'}";
    
            curl_setopt($query_init_curl, CURLOPT_URL,              self::$slack_bot_url);
            curl_setopt($query_init_curl, CURLOPT_RETURNTRANSFER,   true);
            curl_setopt($query_init_curl, CURLOPT_POST,             1);
            curl_setopt($query_init_curl, CURLOPT_POSTFIELDS,       $query_data);
            curl_setopt($query_init_curl, CURLOPT_HTTPHEADER,       $header);
    
            curl_exec($query_init_curl);
            curl_close($query_init_curl);
        } catch (Exception $e) {
            self::sendByDiscord($content);
            self::sendByDiscord('Error in your Slack bot. Detail: '.json_encode($e));
        }
    }
 
    public static function sendByDiscord($content) {
        try {
            $url                = self::$discord_webhooks_url;
            $query_init_curl    = curl_init();
            $header             = ['Content-Type: application/json'];
            $message            = 'Hi. Something went wrong in your application. Some detail here: '. json_encode($content);
            $message_data       = array('content' => $message);
            $message_encode     = json_encode($message_data);

            curl_setopt($query_init_curl, CURLOPT_URL,              $url);
            curl_setopt($query_init_curl, CURLOPT_RETURNTRANSFER,   true);
            curl_setopt($query_init_curl, CURLOPT_POST,             1);
            curl_setopt($query_init_curl, CURLOPT_POSTFIELDS,       $message_encode);
            curl_setopt($query_init_curl, CURLOPT_HTTPHEADER,       $header);

            curl_exec($query_init_curl);
            curl_close($query_init_curl);
        } catch (Exception $e) {
            self::sendBySlack($content);
            self::sendBySlack('Error in your Discord bot. Detail: '.json_encode($e));
        }
    }
}

$message = 'Hello world form log monitor';
LogMonitoring::sendByMail($message);