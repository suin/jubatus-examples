<?php

function get_user_posts(array $data, $page)
{
  $url = 'https://qiita.com/api/v2/users/suin/items?page='.$page.'&per_page=20';
  $result = file_get_contents($url);
  $posts = json_decode($result, true);
  foreach ($posts as $post) {
    $url = $post['url'];
    $title = $post['title'];
    $body = $post['rendered_body'];
    $dom = new DOMDocument;
    @$dom->loadHTML('<?xml encoding="utf-8" ?>'.$body);
    $xpath = new DOMXPath($dom);
    $elems = $xpath->query('//p|//h1|//h2|//h3');
    $text = '';
    foreach ($elems as $elem) {
      $text .= $elem->textContent;
    }
    $data[$url] = $title.'。'.$text;
  }
  return $data;
}

$data = [];
$data = get_user_posts($data, 1);
$data = get_user_posts($data, 2);
$data = get_user_posts($data, 3);
$data = get_user_posts($data, 4);
$data = get_user_posts($data, 5);
file_put_contents(__DIR__ . '/data/training_data.json', json_encode($data, JSON_PRETTY_PRINT|JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES));
