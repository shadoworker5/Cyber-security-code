<?php
/*
* @author Shadoworker5 Dev
* @email shadoworker5.dev@gmail.com
* @create date 2023-01-11 ‏‎23:05:29
* @modify date 2023-01-12 17:17:51
* @desc [description]
*/

class LogMonitoring {
    private $support_address        = 'example@example.xyz';
    private $mail_subject           = 'An Exception occur in your application';
    private $slack_bot_url          = 'https://hooks.slack.com/services/XXXXXXXXX/XXXXXXXXX/XXXXXXXXXXXXXXXXXX';
    private $discord_webhooks_url   = 'https://discordapp.com/api/webhooks/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX';

    public function sendByMail($content) {
        try {
            $message = 'Hi. Something went wrong in your application. Some detail here: '. json_encode($content);
            mail($this->support_address, $this->mail_subject, $message);
        } catch (Exception $e) {
            $this->sendBySlack($content);
            $this->sendBySlack('Error in your Mail user. Detail: '.json_encode($e));
        }
    }

    public function sendBySlack($content) {
        try {
            $query_init_curl    = curl_init();
            $header             = ['Content-Type: application'];
            $query_data         = "{'text': '$content'}";
    
            curl_setopt($query_init_curl, CURLOPT_URL,              $this->slack_bot_url);
            curl_setopt($query_init_curl, CURLOPT_RETURNTRANSFER,   true);
            curl_setopt($query_init_curl, CURLOPT_POST,             1);
            curl_setopt($query_init_curl, CURLOPT_POSTFIELDS,       $query_data);
            curl_setopt($query_init_curl, CURLOPT_HTTPHEADER,       $header);
    
            curl_exec($query_init_curl);
            curl_close($query_init_curl);
        } catch (Exception $e) {
            $this->sendByDiscord($content);
            $this->sendByDiscord('Error in your Slack bot. Detail: '.json_encode($e));
        }
    }
 
    public function sendByDiscord($content) {
        try {
            $url                = $this->discord_webhooks_url;
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
            $this->sendBySlack($content);
            $this->sendBySlack('Error in your Discord bot. Detail: '.json_encode($e));
        }
    }
}

$message = "Hello world form log monitor";
$monitor = new LogMonitoring();
$monitor->sendByMail($message);
echo $message;