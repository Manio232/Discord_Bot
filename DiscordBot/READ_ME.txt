# Discord Bot

## Opis projektu

Ten projekt to prosty bot Discord napisany w Pythonie przy użyciu biblioteki `discord.py`. Bot jest przeznaczony do moderacji serwera, witania nowych użytkowników oraz filtrowania wulgaryzmów.

## Funkcje

- **Powitanie nowych użytkowników**: Bot automatycznie wysyła wiadomość powitalną do nowego członka na kanale powitalnym.
- **Komenda ~hello**: Odpowiada na komendę `~hello` z przywitaniem użytkownika.
- **Filtrowanie wulgaryzmów**: Bot usuwa wiadomości zawierające przekleństwa (takie jak "kurwa", "spierdalaj", "chuj") i wysyła ostrzeżenie użytkownikowi.
- **Logowanie**: Wszystkie zdarzenia są logowane do pliku `discord.log`.

## Wymagania

- Python 3.8 lub nowszy
- Biblioteka `discord.py`
- Biblioteka `python-dotenv` do ładowania zmiennych środowiskowych

## Instalacja

1. Sklonuj repozytorium lub pobierz pliki projektu.

2. Zainstaluj wymagane biblioteki:
   ```
   pip install discord.py python-dotenv
   ```

3. Utwórz konto bota na Discord:
   - Przejdź do [Discord Developer Portal](https://discord.com/developers/applications).
   - Utwórz nową aplikację.
   - Przejdź do zakładki "Bot" i utwórz bota.
   - Skopiuj token bota.

4. Utwórz plik `.env` w katalogu `DiscordBot` i dodaj swój token:
   ```
   DISCORD_TOKEN=twój_token_tutaj
   ```

5. Ustaw ID kanału powitalnego w kodzie `main.py` (zmienna `WELCOME_CHANNEL_ID`).

## Uruchomienie

Uruchom bota za pomocą komendy:
```
python main.py
```

Bot połączy się z Discord i będzie aktywny na serwerze.

## Konfiguracja

- **Prefix komend**: `~`
- **Kanał powitalny**: Ustaw ID kanału w zmiennej `WELCOME_CHANNEL_ID`.
- **Intencje**: Bot używa intencji `message_content` i `members` do obsługi wiadomości i członków.

## Logowanie

Bot loguje wszystkie zdarzenia do pliku `discord.log` w głównym katalogu projektu.

## Uwagi

- Upewnij się, że bot ma odpowiednie uprawnienia na serwerze Discord (zarządzanie wiadomościami, czytanie wiadomości, itp.).
- Dostosuj listę filtrowanych słów w kodzie, jeśli potrzebujesz.

## Licencja

Ten projekt jest open-source. Możesz go modyfikować i używać zgodnie z własnymi potrzebami.
