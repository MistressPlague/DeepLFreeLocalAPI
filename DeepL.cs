using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace Libraries
{
    internal class DeepL
    {
        internal class Language
        {
            internal static readonly string Bulgarian = "Bulgarian";
            internal static readonly string ChineseSimplified = "Chinese (simplified)";
            internal static readonly string Czech = "Czech";
            internal static readonly string Danish = "Danish";
            internal static readonly string Dutch = "Dutch";
            internal static readonly string EnglishUS = "English (American)";
            internal static readonly string EnglishUK = "English (British)";
            internal static readonly string Estonian = "Estonian";
            internal static readonly string Finnish = "Finnish";
            internal static readonly string French = "French";
            internal static readonly string German = "German";
            internal static readonly string Greek = "Greek";
            internal static readonly string Hungarian = "Hungarian";
            internal static readonly string Indonesian = "Indonesian";
            internal static readonly string Italian = "Italian";
            internal static readonly string Japanese = "Japanese";
            internal static readonly string Korean = "Korean";
            internal static readonly string Latvian = "Latvian";
            internal static readonly string Lithuanian = "Lithuanian";
            internal static readonly string Norwegian = "Norwegian (bokmål)";
            internal static readonly string Polish = "Polish";
            internal static readonly string Portuguese = "Portuguese";
            internal static readonly string PortugueseBrazilian = "Portuguese (Brazilian)";
            internal static readonly string Romanian = "Romanian";
            internal static readonly string Russian = "Russian";
            internal static readonly string Slovak = "Slovak";
            internal static readonly string Slovenian = "Slovenian";
            internal static readonly string Spanish = "Spanish";
            internal static readonly string Swedish = "Swedish";
            internal static readonly string Turkish = "Turkish";
            internal static readonly string Ukrainian = "Ukrainian";
        }

        public class TranslationResult
        {
            public string translated_text;
        }

        internal static HttpClient client = new HttpClient();

        internal static async Task<string> TranslateText(string Text, string Language)
        {
            var result = await client.PostAsync("http://127.0.0.1:5000/translate", new StringContent("{\"text\":\"" + Text + "\",\"lang\":\"" + Language + "\"}", Encoding.UTF8, "application/json"));

            return JsonConvert.DeserializeObject<TranslationResult>(await result.Content.ReadAsStringAsync())?.translated_text ?? "";
        }

        internal static string GetLocalLanguageFromAPILanguage(string APILangText)
        {
            switch (APILangText)
            {
                case "en":
                    return Language.EnglishUS;
                case "ja":
                    return Language.Japanese;
                case "zh-CN":
                case "zh-TW":
                case "zh":
                    return Language.ChineseSimplified;
                case "ko":
                    return Language.Korean;
                case "fr":
                    return Language.French;
                case "it":
                    return Language.Italian;
                case "de":
                    return Language.German;
                case "ru":
                    return Language.Russian;
                case "es":
                    return Language.Spanish;
                case "id":
                    return Language.Indonesian;
                case "el":
                    return Language.Greek;
                case "nl":
                    return Language.Dutch;
                case "pt":
                    return Language.Portuguese;
                case "et":
                    return Language.Estonian;
                case "sv":
                    return Language.Swedish;
                case "sk":
                    return Language.Slovak;
                case "sl":
                    return Language.Slovenian;
                case "cs":
                    return Language.Czech;
                case "da":
                    return Language.Danish;
                case "tr":
                    return Language.Turkish;
                case "hu":
                    return Language.Hungarian;
                case "fi":
                    return Language.Finnish;
                case "bg":
                    return Language.Bulgarian;
                case "pl":
                    return Language.Polish;
                case "lv":
                    return Language.Latvian;
                case "lt":
                    return Language.Lithuanian;
                case "ro":
                    return Language.Romanian;
                default:
                    return Language.EnglishUS;
            }
        }
    }
}
