export const createPrompt = (words: string[]) =>
  [
    "以下の単語の日本語風の発音を推定し、指定された形式で出力してください。",
    "他のテキストは含めないでください。",
    "文字の名前で読むことは強く禁止されています（例：'ai'は'エーアイ'ではなく'アイ'です）。",
    "単語の中には略称や頭字語は存在しません。",
    "単語:",
    ...words,
    "形式:",
    "ai=アイ",
    "ui=ウイ",
    "mm=ムム",
    "usb=ウスブ",
    "word=ワード",
    "helmet=ヘルメット",
  ].join("\n");
